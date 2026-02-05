import cv2
import pyautogui
import time

from gesture_detector import GestureDetector
import config

detector = GestureDetector()

cap = cv2.VideoCapture(config.CAMERA_INDEX)

# lower resolution = faster processing
cap.set(3, 480)
cap.set(4, 360)

# timing controls
last_scroll = 0
SCROLL_DELAY = 0.10

paused = False
last_toggle = 0
TOGGLE_DELAY = 0.8

print("Gesture Scroll Started — Press Q to quit")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame, lm = detector.process(frame)
    now = time.time()

    if lm:

        # ✊ fist toggle pause
        if detector.is_fist(lm) and now - last_toggle > TOGGLE_DELAY:
            paused = not paused
            last_toggle = now
            print("PAUSE MODE:", paused)

        if not paused:
            index_y = lm[8][1]
            middle_y = lm[12][1]

            diff = index_y - middle_y

            # scroll up
            if diff < -config.UP_THRESHOLD and now - last_scroll > SCROLL_DELAY:
                pyautogui.scroll(config.SCROLL_AMOUNT)
                last_scroll = now
                print("UP")

            # scroll down
            elif diff > config.DOWN_THRESHOLD and now - last_scroll > SCROLL_DELAY:
                pyautogui.scroll(-config.SCROLL_AMOUNT)
                last_scroll = now
                print("DOWN")

        # status display
        status = "PAUSED" if paused else "ACTIVE"
        cv2.putText(frame, status, (20, 40),
                    cv2.FONT_HERSHEY_SIMPLEX, 1,
                    (0, 0, 255) if paused else (0, 255, 0), 2)

    cv2.imshow("Gesture Scroll", frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
