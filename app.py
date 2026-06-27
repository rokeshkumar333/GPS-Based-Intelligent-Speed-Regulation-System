import base64
import io
import os
import threading
import time
import csv

from flask import Flask, jsonify, request, send_from_directory

try:
    import torch
    import torchvision.transforms as transforms
    from PIL import Image
    from torch import nn
except ImportError:
    torch = None

app = Flask(__name__)

# ===== GLOBAL STATE =====
speed = 0          # km/h (from dashboard / ESP32)
distance = 0       # km (calculated)
helmet = 1         # 1 = ON, 0 = OFF
running = False    # start/stop control
limit = 50
helmet_model = None


class HelmetCNN(nn.Module):
    def __init__(self):
        super().__init__()
        self.features = nn.Sequential(
            nn.Conv2d(3, 16, kernel_size=3, padding=1),
            nn.ReLU(inplace=True),
            nn.MaxPool2d(2),
            nn.Conv2d(16, 32, kernel_size=3, padding=1),
            nn.ReLU(inplace=True),
            nn.MaxPool2d(2),
            nn.Conv2d(32, 64, kernel_size=3, padding=1),
            nn.ReLU(inplace=True),
            nn.MaxPool2d(2)
        )
        self.classifier = nn.Sequential(
            nn.Flatten(),
            nn.Linear(64 * 16 * 16, 128),
            nn.ReLU(inplace=True),
            nn.Dropout(0.3),
            nn.Linear(128, 2)
        )

    def forward(self, x):
        x = self.features(x)
        return self.classifier(x)


def load_helmet_model():
    global helmet_model
    model_path = "helmet_detector.pt"

    if not torch:
        print("[WARN] PyTorch is not installed. Helmet verification will use manual control.")
        return

    if not os.path.exists(model_path):
        print(f"[WARN] Model file not found: {model_path}")
        return

    model = HelmetCNN()
    model.load_state_dict(torch.load(model_path, map_location="cpu"))
    model.eval()
    helmet_model = model
    print("[INFO] Helmet detection model loaded.")


def update_distance_loop():
    global distance, speed, running

    last_time = time.time()
    while True:
        current_time = time.time()
        dt = current_time - last_time
        last_time = current_time

        if running:
            if helmet == 0:
                speed = 0
            elif speed > limit:
                speed = limit

            if speed < 0:
                speed = 0

            distance += (speed * dt) / 3600.0
            distance = round(distance, 5)

            print(f"[LIVE] speed={round(speed,2)} km/h distance={distance} km helmet={helmet}")
            with open("log.csv", "a", newline="") as f:
                writer = csv.writer(f)
                writer.writerow([round(speed, 2), distance, helmet])

        time.sleep(1)


@app.route('/')
def index():
    return send_from_directory('.', 'index.html')


@app.route('/data')
def get_data():
    if helmet == 0:
        current_status = "Helmet Required"
    elif running and speed >= 6:
        current_status = "Speed Controlled"
    elif running:
        current_status = "Running"
    else:
        current_status = "Stopped"

    return jsonify({
        "speed": speed,
        "distance": distance,
        "helmet": helmet,
        "limit": limit,
        "status": current_status,
    })


@app.route('/control', methods=['POST'])
def control():
    global speed, helmet, running, limit
    data = request.json or {}

    if "speed" in data:
        speed = float(data["speed"])

    if "helmet" in data:
        helmet = int(data["helmet"])

    if "start" in data:
        running = bool(data["start"])
        
    if "limit" in data:
        limit = float(data["limit"])

    return jsonify({"status": "ok", "speed": speed, "helmet": helmet, "running": running})


@app.route('/update', methods=['POST'])
def update_from_esp():
    global speed, distance
    data = request.json or {}

    if "speed" in data:
        speed = float(data["speed"])

    if "distance" in data:
        distance = float(data["distance"])

    return jsonify({"status": "updated"})


@app.route('/verify-helmet', methods=['POST'])
def verify_helmet():
    global helmet
    data = request.json or {}
    image_data = data.get("image")
    if not image_data:
        return jsonify({"status": "error", "message": "Missing image"}), 400

    if helmet_model is None:
        return jsonify({"status": "ok", "helmet": helmet, "message": "Model unavailable"})

    try:
        _, encoded = image_data.split(",", 1)
        image_bytes = base64.b64decode(encoded)
        image = Image.open(io.BytesIO(image_bytes)).convert("RGB")

        transform = transforms.Compose([
            transforms.Resize((128, 128)),
            transforms.ToTensor(),
            transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
        ])
        tensor = transform(image).unsqueeze(0)

        with torch.no_grad():
            output = helmet_model(tensor)
            prediction = int(output.argmax(dim=1).item())

        helmet = 1 if prediction == 0 else 0
        message = "Helmet Verified – You can start" if helmet == 1 else "Please wear helmet"
        return jsonify({"status": "ok", "helmet": helmet, "message": message})
    except Exception as exc:
        return jsonify({"status": "error", "message": str(exc)}), 500


if __name__ == "__main__":
    load_helmet_model()
    threading.Thread(target=update_distance_loop, daemon=True).start()
    app.run(host="0.0.0.0", port=5000, debug=True)
