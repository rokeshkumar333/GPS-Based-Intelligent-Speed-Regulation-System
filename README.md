# AI-Based Smart Bike Safety and Speed Control System

This project integrates machine learning, IoT, and embedded system logic to create a smart bike safety system that:
- Verifies helmet usage with a CNN model
- Controls speed dynamically based on safety limits
- Tracks distance in real time
- Provides a web dashboard for start/stop, throttle, and status monitoring

## Project Modules

### Module 1: Helmet Detection
- Dataset path: `helmet-detection/dataset`
- Use `train_helmet_model.py` to train the CNN model
- Trained weights are saved to `helmet_detector.pt`

### Module 2: Dashboard
- Dashboard served by Flask from `index.html`
- Uses webcam video to capture live images for helmet verification
- Displays current speed, distance, helmet status, and ride status

### Module 3: Backend
- Flask app in `app.py`
- Routes:
  - `GET /` → Dashboard page
  - `GET /data` → Real-time speed/distance/status
  - `POST /control` → Update speed, helmet state, start/stop
  - `POST /verify-helmet` → Verify helmet from camera image
  - `POST /update` → Receive ESP32 feedback

### Module 4: IoT Communication
- ESP32 can call `/data` to get current bike state
- Use `/control` to send speed and start/stop commands
- Use `/update` to send actual speed/distance feedback back to Flask

### Module 5: Motor Control Logic
- If helmet is OFF → the system stops motor by setting speed to 0
- If speed reaches or exceeds 6 km/h → backend auto-reduces it to 4 km/h
- Distance is calculated continuously when the ride is running

## Setup

1. Create a Python environment (recommended):
   ```bash
   python -m venv venv
   .\venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install flask pillow torch torchvision
   ```

3. Train the helmet model:
   ```bash
   python train_helmet_model.py
   ```

4. Run the Flask app:
   ```bash
   python app.py
   ```

5. Open the dashboard in a browser:
   ```
   http://127.0.0.1:5000
   ```

## Notes

- If PyTorch is not installed or `helmet_detector.pt` is missing, helmet verification will fall back to manual control in the backend.
- The dashboard requires camera permission for helmet verification.
- The backend currently uses a simple safety rule to reduce speeds at 6 km/h and stop when helmet state is invalid.

## File Summary

- `app.py` — Flask server and IoT API endpoints
- `index.html` — Web dashboard UI
- `train_helmet_model.py` — Helmet detection training script
- `helmet-detection/dataset` — Helmet image dataset
- `README.md` — Project summary and setup instructions
