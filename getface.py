import cv2
import numpy as np


cap = cv2.VideoCapture()

while True:
    _ , img = cap.read()
    cv2.imshow('f'),img