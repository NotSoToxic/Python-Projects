# ✋ Hand Gesture Recognition Using MediaPipe and TensorFlow

This project is a **Hand Gesture Recognition System** built with Python, OpenCV, MediaPipe, and TensorFlow. It captures hand movements from the webcam and recognizes specific gestures using a trained deep learning model.

---

## 🚀 1. Project Overview

- Real-time hand detection using **MediaPipe**.
- Gesture recognition with a pre-trained **TensorFlow** model.
- Displaying gesture names on the webcam feed.
- Supports detection of **single-hand gestures**.

---

## 🛠️ 2. Features

- Real-time gesture prediction.
- High accuracy with MediaPipe landmarks.
- User-friendly interface.
- Easy to train with custom gestures.

---

## 📦 3. Project Structure
```
📦 hand-gesture-recognition 
├─ 📜 gesture_recognition.py # Main Python code 
├─ 📄 gesture.names # Gesture class names 
├─ 🤖 mp_hand_gesture # Trained hand gesture model 
├─ 📂 dataset # (Optional) Dataset for training 
├─ 📷 screenshots/ # Example outputs 
└─ 📃 README.md # Project documentation
```

---

## 📥 4. Installation

Ensure you have **Python 3.8+** installed. Then, install the required dependencies:

```bash
# Create virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate

# Install dependencies
pip install opencv-python numpy mediapipe tensorflow keras
```
