# Crack Detection 1

This repository contains the source code and report for a crack detection program, created for the Calculus 1 (MT1003) course at Ho Chi Minh City University of Technology (Faculty of Applied Science).

## Overview
The program processes digital images (e.g., concrete walls) to automatically detect cracks. It leverages various computer vision algorithms provided by OpenCV to identify meaningful edges and extract the crack's contours.

## Features
- **Advanced Noise Reduction**: Uses a Bilateral Filter to smooth the image while preserving vital edge details.
- **Edge Detection**: Computes adaptive thresholds based on median pixel intensities and applies the Canny edge detector.
- **Morphological Operations**: Uses Closing to seal small gaps in the cracks and Dilation to make them continuous.
- **Contour Detection**: Traces the continuous boundaries of the dilated edges and filters out small artifacts.

## Files
- `crack_detection.py`: The Python script that runs the crack detection algorithm.
- `Calculus_report.pdf`: The detailed assignment report discussing the mathematics, formulas, and processing steps in-depth.
- Various output sample images.

## Requirements
- Python 3.x
- OpenCV (`cv2`)
- NumPy
- Matplotlib

## How to run
1. Ensure the required packages are installed (`pip install opencv-python numpy matplotlib`).
2. Put the target image in the same directory and update the `image_path` variable in `crack_detection.py` (e.g., `image_path = 'canva.jpg'`).
3. Run the script:
   ```bash
   python crack_detection.py
   ```
