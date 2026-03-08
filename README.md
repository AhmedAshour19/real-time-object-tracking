# Real-Time Object Tracking using OpenCV

## Project Overview

This project implements a real-time object tracking system using classical computer vision algorithms provided by OpenCV.

The system allows the user to select a specific object in the first frame using a bounding box. Once the object is selected, the tracker follows the object across subsequent frames in a live webcam feed.

The goal of this project is to demonstrate how traditional tracking algorithms can be applied to track objects in real time without using deep learning models.

---

## Features

- Real-time object tracking using webcam
- Manual object selection using bounding box
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

object-tracking
│
├── src
│ ├── tracker.py
│ └── utils.py
│
├── demo
│ └── demo_video.mp4
│
├── main.py
├── requirements.txt
└── README.md




### File Descriptions

**main.py**

Responsible for running the main application.  
It initializes the webcam, allows the user to select the object, and performs real-time tracking.

**tracker.py**

Contains the `ObjectTracker` class which wraps different OpenCV tracking algorithms and provides a unified interface for initializing, updating, and reinitializing the tracker.

**utils.py**

Contains helper functions used throughout the project such as:

- Drawing bounding boxes
- Displaying text on frames
- Calculating frames per second (FPS)

**demo/demo_video.mp4**

A recorded demonstration of the object tracking system in action.

---

## Installation

Clone the repository:

```bash
git clone https://github.com/AhmedAshour19/object-tracking.git
cd object-tracking
