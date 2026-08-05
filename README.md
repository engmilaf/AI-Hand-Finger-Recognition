# ✋ Hand Finger Recognition Using OpenCV and MediaPipe

## 📌 Project Description

This project is a Computer Vision application designed to recognize human hand fingers in real-time using a webcam.

The system detects the user's hand, tracks finger movements, identifies raised fingers, and displays the number and names of detected fingers on the screen.

The project aims to demonstrate the use of image processing and hand tracking techniques to build an interactive computer vision application.

---

# 🎯 Project Objective

The main objective of this project is to develop a real-time hand finger recognition system using computer vision techniques.

The project aims to:

- Detect the human hand through a webcam.
- Track hand landmarks and finger positions.
- Recognize which fingers are raised.
- Count the number of detected fingers.
- Display the results directly on the video screen.

---

# 🛠 Tools and Technologies Used

| Tool / Technology | Usage |
|-------------------|-------|
| Python | Programming language used to develop the project |
| OpenCV | Used for image processing and webcam access |
| MediaPipe | Used for hand detection and landmark tracking |
| NumPy | Used for numerical operations |
| Anaconda | Used to create and manage the virtual environment |
| Visual Studio Code | Used for writing and running the code |

---

# ⚙️ Project Implementation

The project was implemented through the following steps:

1. Creating a Python virtual environment using Anaconda.
2. Installing the required libraries.
3. Accessing the webcam using OpenCV.
4. Detecting the hand using MediaPipe.
5. Extracting hand landmark points.
6. Analyzing finger positions to determine raised fingers.
7. Displaying the finger count and names on the screen.

---

# ⚠️ Problems Faced and Solutions

## 1. MediaPipe Installation Problem

### Problem:
During the installation process, MediaPipe was not working correctly due to compatibility issues between the package version and the Python environment.

### Solution:
A compatible version of MediaPipe was installed:
pip install mediapipe==0.10.21

---

## 2. OpenCV and MediaPipe Compatibility Issue

### Problem:
Some OpenCV versions caused errors when running the hand tracking system.

### Solution:
A stable OpenCV version was installed to ensure compatibility:
pip install opencv-python==4.10.0.84

---

## 3. Python Environment Not Recognized in Visual Studio Code

### Problem:
Visual Studio Code could not access the installed libraries because it was using a different Python interpreter.

### Solution:
The correct Anaconda environment was selected:
Python 3.10 (hand_recognition)

---

## 4. Camera Did Not Stop After Running

### Problem:
The webcam continued running after closing the program.

### Solution:
The application was stopped by:
- Pressing the **Q** key while the camera window was active.
- Using **Ctrl + C** in the terminal.

---

# 📷 Project Experiment Results

The following images show the results of testing the hand finger recognition system using different hand gestures.

**Website:** https://milaf.free.je/index3.html



