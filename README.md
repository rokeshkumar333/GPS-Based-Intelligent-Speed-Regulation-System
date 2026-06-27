# 🚀 AI-Based Smart Bike Safety and Speed Control System

An **Artificial Intelligence (AI)** and **Internet of Things (IoT)** based intelligent transportation system designed to improve rider safety through **Helmet Detection**, **Machine Learning**, **ESP32**, **Arduino Nano**, and a **Flask-based Web Dashboard**.

The project integrates Computer Vision, Embedded Systems, and Web Technologies to create a smart bike safety solution capable of monitoring rider status, controlling vehicle speed, and displaying real-time information.

---

# 📷 Project Demonstration

## Dashboard - Route selection

![Dashboard 1](Dashboard%201.png)

---

## Dashboard - speed control

![Dashboard 2](Dashboard%202.png)

---

## System Architecture

![System Architecture](System%20Architecture.png)

---

# 🎯 Project Objectives

- Improve rider safety using Artificial Intelligence.
- Detect helmet usage before allowing vehicle movement.
- Monitor and regulate vehicle speed.
- Communicate between Flask, ESP32, and Arduino Nano.
- Demonstrate the integration of AI, IoT, and Embedded Systems.
- Build an intelligent transportation prototype for academic research.

---

# ✨ Features

- 🛡 Helmet Detection using Deep Learning
- 🌍 GPS-Based Route Monitoring
- 🚦 Intelligent Speed Regulation
- 📊 Real-time Dashboard
- 📷 Live Camera Integration
- 📈 Distance Tracking
- ⚡ Flask REST API
- 🔗 ESP32 Communication
- 🤖 Arduino Nano Motor Control
- 📁 Data Logging
- 🧠 Machine Learning Models
- 🚨 Safety Rule Engine

---

# 🏗 System Architecture

The system consists of six major modules:

### 1. AI Helmet Detection
- Detects whether the rider is wearing a helmet.
- Uses a CNN-based deep learning model.
- Returns Helmet / No Helmet prediction.

---

### 2. Flask Backend

Responsible for

- Processing dashboard requests
- Managing speed
- Helmet verification
- Distance calculation
- REST API communication
- Logging vehicle information

---

### 3. Web Dashboard

Provides

- Route Visualization
- Helmet Detection
- Start / Stop Control
- Speed Display
- Distance Display
- Ride Status
- Throttle Control

---

### 4. ESP32

Responsible for

- Receiving commands from Flask
- Sending live data
- Communicating with Arduino Nano

---

### 5. Arduino Nano

Responsible for

- Controlling the motor
- Receiving ESP32 commands
- Executing speed regulation

---

### 6. Machine Learning Module

Includes

- Helmet Detection
- Traffic Prediction
- Rash Driving Detection
- Anomaly Detection

---

# 🛠 Technologies Used

## Programming Languages

- Python
- HTML
- CSS
- JavaScript
- C++

---

## Frameworks

- Flask
- OpenCV
- PyTorch
- TorchVision

---

## Libraries

- NumPy
- Pillow
- Pandas

---

## Hardware

- ESP32
- Arduino Nano
- Camera
- DC Motor
- Motor Driver

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
├── logs/
│     log.csv
│
├── ml_models/
│     anomaly_model.py
│     traffic_model.py
│     rash_model.py
│     train_helmet_model.py
│
├── models/
│     helmet_detector.pt
│
├── templates/
│     index.html
│
├── Dashboard 1.png
├── Dashboard 2.png
├── System Architecture.png
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

# 🔄 System Workflow

1. User opens the Flask Dashboard.
2. Camera captures rider image.
3. AI verifies helmet usage.
4. Flask processes safety rules.
5. ESP32 receives commands.
6. Arduino Nano controls the motor.
7. Dashboard continuously updates:
   - Current Speed
   - Distance
   - Helmet Status
   - Ride Status

---

# ⚡ Safety Rules

The system follows these rules:

- If Helmet = No Helmet → Vehicle cannot move.
- Speed is continuously monitored.
- Vehicle status is displayed on the dashboard.
- Ride information is logged.

---

# 🌐 Flask API

| Method | Endpoint | Description |
|----------|-----------|----------------------------|
| GET | / | Dashboard |
| GET | /data | Live Vehicle Data |
| POST | /control | Control Vehicle |
| POST | /verify-helmet | Helmet Verification |
| POST | /update | Receive ESP32 Feedback |

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

## Run Flask

```bash
python app.py
```

---

Open Browser

```
http://127.0.0.1:5000
```

---

# 📊 Dataset

The helmet detection model was trained using approximately **300 helmet and non-helmet images**.

The dataset is **not included** in this repository because of GitHub file size limitations.

Users can train the model using their own dataset by running:

```bash
python train_helmet_model.py
```

---

# 📈 Future Improvements

- Google Maps API Integration
- Live GPS Tracking
- Cloud Database
- Mobile Application
- Traffic Prediction
- Voice Assistant
- Emergency SOS
- Accident Detection
- Real Bike Prototype Integration

---

# 👨‍💻 Author

**Rokesh Kumar K**

B.Tech – Artificial Intelligence & Data Science

SRM Valliammai Engineering College

GitHub:
https://github.com/rokeshkumar333

---

# ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.
