# Real-Time Object Tracking

---

## 1. Project Idea

This project is a real-time object tracking system using OpenCV.  
The user can select an object in the first frame of the webcam video, and the system will track this object as it moves across subsequent frames.

---

## 2. Technique Used

The project uses the **CSRT (Channel and Spatial Reliability Tracker)** algorithm from OpenCV.  
**How it works in brief:**  
- CSRT estimates the position of the object in each frame by learning a correlation filter.  
- It combines information from multiple channels and evaluates spatial reliability to track objects more accurately.  
- CSRT is more robust than other classical trackers like KCF or MOSSE, especially for objects with scale changes or partial occlusion.

---

## 3. How the System Works

1. The webcam captures video frames continuously.  
2. The user selects the object to track using a bounding box.  
3. The CSRT tracker initializes with the selected region.  
4. For each new frame, the tracker updates the position of the object.  
5. A bounding box is drawn around the tracked object to visualize tracking.  
6. If tracking fails, the user can press **R** to reselect the object.

---

## 4. How to Download and Run

```bash
# Step 1: Clone the repository
git clone https://github.com/AhmedAshour19/real-time-object-tracking
.git
cd object-tracking

# Step 2: Install the dependencies
pip install -r requirements.txt

# Step 3: Run the project
python main.py
