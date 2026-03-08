# Real-Time Object Tracking using OpenCV

## Project Overview

This project implements a real-time object tracking system using classical computer vision algorithms provided by OpenCV.

The system allows the user to select a specific object in the first frame using a bounding box. Once the object is selected, the tracker follows the object across subsequent frames in a live webcam feed.

The goal of this project is to demonstrate how traditional tracking algorithms can be applied to track objects in real time without using deep learning models.

---

## Features

- Real-time object tracking using webcam
- Manual object selection using a bounding box
- Multiple OpenCV tracking algorithms supported
- Ability to reinitialize tracking if tracking is lost
- Live visualization of the tracking bounding box
- FPS counter to monitor real-time performance

---

## Tracking Algorithms

The system supports several tracking algorithms available in OpenCV:

- CSRT (default – high accuracy)
- KCF
- MIL
- Boosting
- TLD
- MedianFlow
- MOSSE

Among these trackers, **CSRT** was chosen as the default tracker because it provides better accuracy and robustness compared to other classical trackers.

---

## Project Structure

```
object-tracking
│
├── src
│   ├── tracker.py
│   └── utils.py
│
├── demo
│   └── demo_video.mp4
│
├── main.py
├── requirements.txt
└── README.md
```

---

## File Descriptions

### main.py

This file is responsible for running the main application.  
It initializes the webcam, allows the user to select the object, and performs real-time tracking.

Main responsibilities include:

- Opening the webcam stream
- Allowing the user to select an object using a bounding box
- Initializing the tracker
- Updating the tracker for each video frame
- Displaying the tracking results in real time

---

### tracker.py

This file contains the **ObjectTracker class**, which wraps different OpenCV tracking algorithms and provides a unified interface for:

- Tracker initialization
- Tracker updating
- Tracker reinitialization

This design allows easy switching between different tracking algorithms.

---

### utils.py

This file contains helper functions used throughout the project, such as:

- Drawing bounding boxes around tracked objects
- Displaying text information on video frames
- Calculating frames per second (FPS)

These functions help keep the main code clean and modular.

---

### demo/demo_video.mp4

This file contains a recorded demonstration showing the tracking system working on a live webcam feed.

---

## Installation

Clone the repository:

```bash
git clone https://github.com/AhmedAshour19/object-tracking.git
cd object-tracking
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

---

## Running the Project

Run the following command:

```bash
python main.py
```

After running the program:

1. The webcam will start.
2. Select the object to track using a bounding box.
3. The tracker will begin following the object in real time.

---

## How the System Works

1. The webcam captures video frames continuously.
2. The user selects the object to track using a bounding box.
3. The tracker is initialized with the selected region of interest (ROI).
4. For every new frame, the tracker updates the position of the object.
5. A bounding box is drawn around the tracked object.
6. If the tracker loses the object, the user can press **R** to reselect it.

---

## Performance

The system runs in real time on CPU using classical OpenCV tracking algorithms.

An FPS counter is displayed during execution to monitor the performance of the tracking process.

---

## Demo

A demonstration video showing the system working in real time is available in the `demo` folder.

---

## Future Improvements

Possible improvements to the system include:

- Integrating deep learning based trackers
- Supporting multi-object tracking
- Adding automatic object detection before tracking
- Improving the user interface

