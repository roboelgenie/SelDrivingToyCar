import cv2
import datetime
import csv
import os
import serial
import time
import numpy as np
import tensorflow
# from tensorflow import keras
# from tensorflow._api.v2.keras import layers
# from tensorflow.keras.models import load_model

load_model = tensorflow.keras.models.load_model

model_path = 'Model/model.h5'
model = load_model(model_path)

cap = cv2.VideoCapture(1)

if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

while True:
    ret, frame = cap.read()

    if not ret:
        print("Error: Could not read frame.")
        break
    cv2.imshow("Frame", frame)
    frame = np.asarray(frame)
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2YUV)
    frame = cv2.GaussianBlur(frame, (3, 3), 0)
    frame = cv2.resize(frame, (200, 140))
    frame = frame / 255

    # input_data = np.expand_dims(frame, axis=0)
    frame = np.array([frame])
    prediction = float(model.predict(frame))

    # prediction = model.predict(input_data)[0]


    print("Prediction:", prediction)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera, close the serial port, close the CSV file, and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
