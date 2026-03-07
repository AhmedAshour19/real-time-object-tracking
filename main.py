import cv2
from src.tracker import ObjectTracker
from src.utils import draw_bbox, draw_text, FPS


def main():

    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Cannot access camera")
        return

    ret, frame = cap.read()

    if not ret:
        print("Error: Cannot read frame")
        return

    tracker = ObjectTracker(tracker_type="csrt")

    bbox = cv2.selectROI("Select Object to Track", frame, False)

    tracker.initialize(frame, bbox)

    cv2.destroyWindow("Select Object to Track")

    fps_counter = FPS()

    while True:

        ret, frame = cap.read()
        if not ret:
            break

        success, bbox = tracker.update(frame)

        if success:

            draw_bbox(frame, bbox)

            draw_text(
                frame,
                f"{tracker.tracker_name.upper()} Tracker",
                (10, 30)
            )

        else:

            draw_text(
                frame,
                "Tracking Lost! Press R to reselect",
                (10, 30)
            )

        fps = fps_counter.update()

        draw_text(
            frame,
            f"FPS: {fps:.2f}",
            (10, 60)
        )

        cv2.imshow("Object Tracker", frame)

        key = cv2.waitKey(1) & 0xFF

        if key == ord("q"):
            break

        elif key == ord("r"):

            bbox = cv2.selectROI("Reselect Object", frame, False)

            tracker.reinitialize(frame, bbox)

            cv2.destroyWindow("Reselect Object")

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
