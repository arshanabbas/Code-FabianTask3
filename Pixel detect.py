# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 13:13:43 2024

@author: arab
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

def get_pixel_color(image_path, x, y):
   
    # Load the image using OpenCV
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    
    # Get the color value of the pixel at coordinates (x, y)
    pixel_color = image[y, x]
    
    return pixel_color

# Example usage:
image_path = "F:/Arshan_Abbas/Fabian/Task3/Img/1.jpg"
x_coordinate = 50
y_coordinate = 3000
pixel_color = get_pixel_color(image_path, x_coordinate, y_coordinate)
print("Color value at coordinates (x={}, y={}): {}".format(x_coordinate, y_coordinate, pixel_color))

# Save the registered image
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
plt.scatter(x_coordinate, y_coordinate)
cv2.imwrite("F:/Arshan_Abbas/Fabian/Task3/Img/image4.jpg", image)
