# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 11:13:48 2024

@author: arab
"""
import numpy as np
import matplotlib.pyplot as plt
import cv2
import math
from PIL import Image
import imutils

image_original = cv2.imread("1.jpg")  # Replace with the path to your image

image = cv2.cvtColor(image_original, cv2.COLOR_BGR2GRAY)

x_start, x_end = 2110, 2121
y_start, y_end = 1670, 1690

selected_portion1 = image[y_start:y_end, x_start:x_end]

coordinates = []
threshold = 105
first_values = []

for y, row in enumerate(selected_portion1):
    found = False
    for x, value in enumerate(row):
        if value > threshold:
            first_values.append(value)
            coordinates.append((x, y))
            found = True
            break
    if not found:
        first_values.append(None)
        coordinates.append(None)

print(first_values) #print 1 

#select only values which are not None
coordinates = [coord for coord in coordinates if coord is not None]

for coord in coordinates:
    x, y = coord
    cv2.circle(image, (x, y), radius=3, color=(255, 0, 0), thickness=-1)
    
cv2.imwrite("Image&dots.jpg", image)

num_first_values = len(first_values)
print(num_first_values) #print 2

num_coordinates_count = len(coordinates)
print(num_coordinates_count) #print 3

print(coordinates) #print 4