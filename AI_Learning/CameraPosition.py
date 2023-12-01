import os
import cv2
import csv
import serial
import datetime

# Open the default camera (index 0)
cap = cv2.VideoCapture(1)

# Check if the camera opened successfully
if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()
# !!ONLY for camera test. Comoent for training!!
while True:
    ret, frame = cap.read()
    cv2.imshow("Frame", frame)
    # Check if the frame was read successfully
    if not ret:
        print("Error: Could not read frame.")
        break
#Break the loop if 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# !!ONLY for camera test. Comoent for training!!

# Release the camera and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()