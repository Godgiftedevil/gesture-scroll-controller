import cv2
import mediapipe as mp


class GestureDetector:
    def __init__(self):
        self.mp_hands = mp.solutions.hands

        # ⚡ faster model settings
        self.hands = self.mp_hands.Hands(
            max_num_hands=1,
            model_complexity=0,
            min_detection_confidence=0.6,
            min_tracking_confidence=0.6
        )

        self.drawer = mp.solutions.drawing_utils
        self.draw_landmarks = False   # speed boost — True karega to lines dikhenge

    def process(self, frame):
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.hands.process(rgb)

        landmarks = None

        if results.multi_hand_landmarks:
            hand = results.multi_hand_landmarks[0]
            h, w, _ = frame.shape

            landmarks = []
            for lm in hand.landmark:
                landmarks.append((int(lm.x * w), int(lm.y * h)))

            # optional drawing (slow)
            if self.draw_landmarks:
                self.drawer.draw_landmarks(
                    frame,
                    hand,
                    self.mp_hands.HAND_CONNECTIONS
                )

        return frame, landmarks

    # ✊ FIST DETECTION
    def is_fist(self, lm):
        if not lm:
            return False

        tips = [8, 12, 16, 20]
        joints = [6, 10, 14, 18]

        folded = 0
        for t, j in zip(tips, joints):
            if lm[t][1] > lm[j][1]:
                folded += 1

        return folded >= 3
