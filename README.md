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
