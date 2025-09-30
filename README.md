# 🧑‍💻 Face Recognition Project (OpenCV + Haar Cascades)

A real-time **face detection and recognition system** built with **OpenCV** and **Haar Cascades**.
This project allows you to **create a dataset**, **train a face recognizer**, and **recognize faces in real-time** using your webcam.

---

## 📦 Tech Stack

* **Python 3** – Core language
* **OpenCV** – Real-time computer vision
* **Haar Cascades** – Pre-trained face detection model
* **LBPH Face Recognizer** – Basic face recognition
* **SQLite** – Lightweight database to store user info
* **Optional upgrades:** DeepFace, FaceNet, dlib, or DNN models for higher accuracy

---

## 🗂️ Folder Structure

```
Face_recognition/
├── dataset/                    # Captured face images for training
├── dataset_creater.py           # Script to capture face datasets
├── detect.py                    # Real-time face detection & recognition
├── trainer.py                   # Train the LBPH face recognizer
├── recognizer/                  # Trained model files
├── FaceBase.db                  # SQLite database storing user details
├── haarcascade_frontalface_default.xml  # Haar Cascade model
├── requirements.txt             # Python dependencies
├── README.md                    # Project documentation
└── venv/                        # Virtual environment
```

---

## 🚀 Features

* Real-time **face detection** using OpenCV.
* **Create and manage custom face datasets** for multiple users.
* Store and retrieve **user information** from an SQLite database.
* Train and **recognize faces** using LBPH recognizer.
* Extendable to advanced recognition models (DeepFace, FaceNet, DNN).

---

## ⚙️ Installation

```bash
# Clone the repository
git clone https://github.com/your-username/Face_Recognition.git
cd Face_Recognition

# Create virtual environment
python3 -m venv venv
source venv/bin/activate       # Linux/macOS
venv\Scripts\activate          # Windows

# Install dependencies
pip install -r requirements.txt
```

---

## 🏗️ Usage

1. **Create a dataset** for a new user:

```bash
python dataset_creater.py
```

2. **Train the recognizer**:

```bash
python trainer.py
```

3. **Detect & recognize faces** in real-time:

```bash
python detect.py
```

> Make sure your webcam is connected for real-time detection.

---

## 📊 Accuracy & Improvements

* **Current model:** Haar Cascade + LBPH
* **Accuracy depends on:** dataset size, lighting conditions, and image quality.
* **How to improve:**

  * Use **DNN-based models** (OpenCV DNN with ResNet, Caffe, or TensorFlow).
  * Use **FaceNet, DeepFace, or dlib embeddings** for more robust recognition.
  * Collect **diverse datasets per person** (different angles, lighting, expressions).
  * Evaluate recognition accuracy using **precision, recall, F1-score**.

---

## ⚠️ Limitations

* LBPH performs well for controlled environments but struggles in **low-light** or **crowded scenes**.
* Haar Cascade detection can produce **false positives** for non-face objects.

---

## 🙋‍♂️ Author

Built by **Himanshu Yadav** as part of a computer vision project to learn **real-time face recognition** and dataset management.

