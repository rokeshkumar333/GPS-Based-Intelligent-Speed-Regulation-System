# 🚀 AI-Based Smart Bike Safety and Speed Control System

An Artificial Intelligence (AI) and Internet of Things (IoT) based intelligent transportation system designed to improve rider safety by integrating **Helmet Detection**, **Dynamic Speed Regulation**, **ESP32**, **Arduino Nano**, **Flask**, and **Machine Learning**.

This project demonstrates how Computer Vision, Embedded Systems, and Web Technologies can work together to create a smart and safer riding experience.

---

# 📷 Project Demonstration

## Dashboard

![Dashboard](images/dashboard.png)

---

## System Architecture

![Architecture](images/architecture.png)

---

## 🎯 Project Objectives

- Improve rider safety using AI.
- Prevent bike operation without helmet verification.
- Dynamically regulate vehicle speed.
- Monitor vehicle speed and travel distance.
- Integrate Machine Learning with IoT.
- Demonstrate intelligent transportation concepts.

---

# ✨ Features

✅ Helmet Detection using Deep Learning

✅ Flask Web Dashboard

✅ ESP32 and Arduino Nano Communication

✅ Dynamic Speed Control

✅ Real-time Speed Monitoring

✅ Distance Calculation

✅ Machine Learning Integration

✅ REST API Communication

✅ Safety Rule Engine

---

# 🛠 Technologies Used

## Programming Languages

- Python
- HTML
- CSS
- JavaScript
- C++ (Arduino)

---

## Frameworks & Libraries

- Flask
- OpenCV
- PyTorch
- TorchVision
- NumPy
- Pillow

---

## Hardware

- ESP32
- Arduino Nano
- DC Motor
- Motor Driver
- Camera Module

---

## Development Tools

- VS Code
- Arduino IDE
- Git
- GitHub

---

# 📂 Project Structure

```
GPS-Based-Intelligent-Speed-Regulation-System

│
├── arduino_nano/
│
├── esp32/
│
├── helmet-detection/
│
├── logs/
│      log.csv
│
├── ml_models/
│      anomaly_model.py
│      traffic_model.py
│      rash_model.py
│      train_helmet_model.py
│
├── models/
│      helmet_detector.pt
│
├── templates/
│      index.html
│
├── app.py
├── README.md
├── requirements.txt
└── .gitignore
```

---

# ⚙️ System Workflow

1. Rider starts the dashboard.
2. Camera verifies helmet usage.
3. Flask backend processes the helmet status.
4. ESP32 communicates with Arduino Nano.
5. Speed commands are sent to the motor.
6. Real-time dashboard displays:
   - Current Speed
   - Distance Travelled
   - Helmet Status
   - Ride Status
7. Safety rules automatically reduce or stop the vehicle when necessary.

---

# 🧠 Machine Learning Module

The project uses a Convolutional Neural Network (CNN) based helmet detection model.

### Training

```
python train_helmet_model.py
```

The trained model is stored as

```
helmet_detector.pt
```

---

# 🌐 Flask API

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | `/` | Dashboard |
| GET | `/data` | Get Live Data |
| POST | `/control` | Control Speed |
| POST | `/verify-helmet` | Helmet Verification |
| POST | `/update` | ESP32 Feedback |

---

# ⚡ Safety Logic

The system follows the following safety rules:

- Bike will not start without helmet verification.
- Speed is monitored continuously.
- If safety limits are exceeded, speed is automatically reduced.
- Distance is calculated throughout the ride.

---

# 🚀 Installation

## Clone Repository

```bash
git clone https://github.com/rokeshkumar333/GPS-Based-Intelligent-Speed-Regulation-System.git
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run the Flask Application

```bash
python app.py
```

---

Open your browser

```
http://127.0.0.1:5000
```

---

# 📊 Dataset

The helmet detection model was trained using approximately **300 helmet and non-helmet images**.

The dataset is **not included** in this repository because of GitHub file size limitations.

Users can train the model using their own dataset by running

```bash
python train_helmet_model.py
```

---

# 🔮 Future Improvements

- Google Maps API Integration
- Live GPS Tracking
- Traffic Prediction
- Mobile Application
- Cloud Database Integration
- Emergency SOS Alert
- Voice Assistant
- Automatic Accident Detection

---

# 👨‍💻 Author

**Rokesh Kumar K**

B.Tech – Artificial Intelligence & Data Science

SRM Valliammai Engineering College

GitHub:
https://github.com/rokeshkumar333

---

# ⭐ If you found this project useful, please consider giving it a star!
