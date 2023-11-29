import numpy as np
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

#Open arduino comunication
arduino = serial.Serial(port='COM4',   baudrate=115200, timeout=.1)

# Create a directory to store the captured frames
output_directory = "captured_frames"
os.makedirs(output_directory, exist_ok=True)

csv_filename = "timestamps.csv"
csv_path = os.path.join(output_directory, csv_filename)

with open(csv_path, mode='w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    # csv_writer.writerow(["Timestamp"])

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Check if the frame was read successfully
        if not ret:
            print("Error: Could not read frame.")
            break

        # Get the current timestamp
        timestamp = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S_%f")[:-3]  # milliseconds precision

        # Save the frame as a JPG file with the timestamp as the filename
        filename = os.path.join(output_directory, f"{timestamp}.jpg")
        cv2.imwrite(filename, frame)

        # Display the frame
        cv2.imshow("Frame", frame)

        csv_writer.writerow([timestamp])

        # Break the loop if 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# Release the camera and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()