# 🖐 Gesture Scroll Controller (Python + MediaPipe)

<p align="center">
  <img src="demo.gif" width="700">
</p>


Control page scrolling using hand gestures through your webcam — no mouse wheel needed.

This project uses Computer Vision + MediaPipe hand tracking to detect finger positions and trigger scroll actions in real time. Built as a beginner-friendly but portfolio-level practical CV project.

---

# 🚀 Features

* Hand tracking using MediaPipe
* Scroll up / down using finger gesture
* Fast response optimized
* Separate sensitivity for up/down gestures
* Fist gesture = Pause / Resume control
* Smooth scroll cooldown system
* Low resolution mode for better FPS
* Modular multi-file Python structure
* Windows EXE build supported

---

# 🧠 How It Works (Simple)

Camera detects your hand → tracks finger landmarks → compares index & middle finger height → triggers scroll.

Logic:

* Index finger above middle → Scroll Up
* Index finger below middle → Scroll Down
* Fist → Toggle Pause Mode

---

# 📦 Requirements

Recommended Python version: **3.10 – 3.12**

Install dependencies:

```
pip install -r requirements.txt
```

If you don’t have requirements.txt yet, create it with:

```
opencv-python
mediapipe==0.10.9
pyautogui
```

---

# 📁 Project Structure

```
gesture-scroll-controller/
│
├── main.py
├── gesture_detector.py
├── config.py
├── requirements.txt
└── README.md
```

---

# ▶ Run the Project

Open terminal inside the project folder:

```
python main.py
```

Camera window will open and gesture control will start.

Press **Q** to quit.

---

# ✋ Gesture Controls

| Gesture                         | Action         |
| ------------------------------- | -------------- |
| Index finger higher than middle | Scroll Up      |
| Index finger lower than middle  | Scroll Down    |
| Fist                            | Pause / Resume |
| Keyboard Q                      | Exit app       |

Status text (ACTIVE / PAUSED) is shown on screen.

---

# ⚙ Sensitivity & Speed Tuning

Open `config.py`:

```
SCROLL_AMOUNT = 60
UP_THRESHOLD = 20
DOWN_THRESHOLD = 14
CAMERA_INDEX = 0
```

Tuning guide:

* Lower threshold → faster trigger
* Higher threshold → safer trigger
* Increase SCROLL_AMOUNT → bigger scroll jump
* Decrease SCROLL_AMOUNT → smoother scroll

In main.py:

```
SCROLL_DELAY = 0.10
```

Lower = faster repeat scroll
Higher = more controlled scroll

---

# ⚡ Performance Optimizations Used

* Camera resolution reduced (480×360)
* MediaPipe model_complexity = 0 (fast model)
* Landmark drawing disabled
* Scroll cooldown timer added
* Separate up/down thresholds
* Tracking confidence tuned

---

# 🛠 Build Windows EXE

Install PyInstaller:

```
pip install pyinstaller
```

IMPORTANT build command (MediaPipe fix included):

```
python -m PyInstaller --onefile --collect-all mediapipe main.py
```

After build completes:

```
dist/main.exe
```

Double click to run like a normal desktop app.

Note: EXE size may be large (150–300MB) because MediaPipe is heavy.

---

# ❗ Common Errors & Fixes (Real Issues Faced During Build)

## 🔴 mediapipe has no attribute solutions

Cause: New MediaPipe versions changed API.

Fix:

```
pip uninstall mediapipe
pip install mediapipe==0.10.9
```

---

## 🔴 pyinstaller not recognized

Fix:

```
python -m PyInstaller --onefile main.py
```

---

## 🔴 EXE crashes with mediapipe FileNotFoundError

Fix build command:

```
python -m PyInstaller --onefile --collect-all mediapipe main.py
```

---

## 🔴 Scroll down reacts slower than scroll up

Fix: Use separate thresholds:

```
UP_THRESHOLD = 20
DOWN_THRESHOLD = 14
```

And reduce:

```
SCROLL_DELAY = 0.10
```

---

## 🔴 Files saved as main.py.txt instead of .py

Windows hides extensions.

Fix:

Explorer → View → Show → File name extensions → rename properly.

---

## 🔴 Camera opens but gesture laggy

Improve speed:

* Reduce camera resolution
* Disable landmark drawing
* Lower thresholds slightly
* Lower SCROLL_DELAY

---

# 🎓 Concepts Demonstrated

* Computer Vision basics
* Hand landmark detection
* Gesture recognition logic
* Real-time input control
* Performance tuning
* Modular Python architecture
* Dependency debugging
* EXE packaging with PyInstaller

---

# 🔮 Possible Future Upgrades

* Gesture grid UI
* Air click system
* Voice typing mode
* System tray background app
* Tab switching gestures
* Full desktop gesture control

---

# 👨‍💻 Author Note

Built as a learning + portfolio project to explore real-time gesture-based interaction using Python and MediaPipe.
