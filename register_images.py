# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 12:24:17 2024

@author: arab
"""

import cv2
import numpy as np

def register_images(image1, image2):
    # Convert images to grayscale
    gray1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
    
    # Initialize ORB detector
    orb = cv2.ORB_create()
    
    # Find keypoints and descriptors
    keypoints1, descriptors1 = orb.detectAndCompute(gray1, None)
    keypoints2, descriptors2 = orb.detectAndCompute(gray2, None)
    
    # Initialize Brute-Force matcher
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    
    # Match descriptors
    matches = bf.match(descriptors1, descriptors2)
    
    # Sort matches based on their distances
    matches = sorted(matches, key=lambda x: x.distance)
    
    # Draw top matches
    matched_img = cv2.drawMatches(image1, keypoints1, image2, keypoints2, matches[:10], None, flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
    
    # Save the registered image
    cv2.imwrite("R:/Arshan Abbas/Image_overlay/Images/registered_image7.jpg", matched_img)

# Load images
image1 = cv2.imread("R:/Arshan Abbas/Image_overlay/Images/W4-1-S1-Kalling2-NEU.jpg")
image2 = cv2.imread("R:/Arshan Abbas/Image_overlay/Images/W4-1-S1-NEU.jpg")

# Perform image registration
register_images(image1, image2)


