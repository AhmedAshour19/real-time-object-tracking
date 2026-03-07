import cv2
import time


def draw_bbox(frame, bbox):

    x, y, w, h = [int(v) for v in bbox]

    cv2.rectangle(frame,
                  (x, y),
                  (x + w, y + h),
                  (0, 255, 0),
                  2)


def draw_text(frame, text, position=(10, 30)):

    cv2.putText(frame,
                text,
                position,
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (0, 255, 0),
                2)


class FPS:

    def __init__(self):
        self.start_time = time.time()
        self.frame_count = 0

    def update(self):

        self.frame_count += 1
        elapsed = time.time() - self.start_time

        if elapsed > 0:
            return self.frame_count / elapsed

        return 0
