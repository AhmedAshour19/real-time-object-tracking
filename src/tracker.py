import cv2


class ObjectTracker:

    def __init__(self, tracker_type="csrt"):

        self.tracker_name = tracker_type

        self.tracker_dict = {

            "csrt": cv2.legacy.TrackerCSRT_create,
            "kcf": cv2.legacy.TrackerKCF_create,
            "mil": cv2.legacy.TrackerMIL_create,
            "boosting": cv2.legacy.TrackerBoosting_create,
            "tld": cv2.legacy.TrackerTLD_create,
            "medianflow": cv2.legacy.TrackerMedianFlow_create,
            "mosse": cv2.legacy.TrackerMOSSE_create

        }

        if tracker_type not in self.tracker_dict:
            raise ValueError("Unsupported tracker type")

        self.tracker = self.tracker_dict[self.tracker_name]()

    def initialize(self, frame, bbox):

        self.tracker.init(frame, bbox)

    def update(self, frame):

        return self.tracker.update(frame)

    def reinitialize(self, frame, bbox):

        self.tracker = self.tracker_dict[self.tracker_name]()
        self.tracker.init(frame, bbox)
