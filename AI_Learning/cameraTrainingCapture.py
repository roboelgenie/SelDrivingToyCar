import numpy as np
import os
import cv2
import csv
import serial
import datetime


cap = cv2.VideoCapture(1)

if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()
#!!ONLY for camera test. Comoent for training!!
# while True:
#     ret, frame = cap.read()
#     cv2.imshow("Frame", frame)

#     if not ret:
#         print("Error: Could not read frame.")
#         break

#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#!!ONLY for camera test. Comoent for training!!

arduino = serial.Serial(port='COM4', baudrate=9600, timeout=.1)

def ardRead():
    try:
        line = arduino.readline().decode('utf-8').strip()

        print("Received:", line)
        return line

    except KeyboardInterrupt:
        arduino.close()
        print("Serial port closed.")

output_directory = "captured_frames"
os.makedirs(output_directory, exist_ok=True)

csv_filename = "timestamps_raw.csv"
csv_path = os.path.join(output_directory, csv_filename)

with open(csv_path, mode='w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file, escapechar=' ', quoting=csv.QUOTE_NONE)
    # csv_writer.writerow(["Timestamp"])

    while True:
        ret, frame = cap.read()

        if not ret:
            print("Error: Could not read frame.")
            break

        timestamp = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S_%f")[:-3]
        filename = os.path.join(output_directory, f"{timestamp}.jpg")

        cv2.imwrite(filename, frame)
        cv2.imshow("Frame", frame)

        steering = ardRead()

        csv_writer.writerow([timestamp + '.jpg'] + [steering])

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
arduino.close()
cv2.destroyAllWindows()