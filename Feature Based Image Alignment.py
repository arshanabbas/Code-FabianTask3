# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 13:22:31 2024

@author: arab
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

refFilename = "R:/Arshan Abbas/Image_overlay/Images/W4-1-S1-Kalling2-NEU.jpg"
print("Reading:", refFilename)
im1 = cv2.imread(refFilename, cv2.IMREAD_COLOR)
im1 = cv2.cvtColor(im1, cv2.COLOR_BGR2RGB)

#Read image to be aligned
imFilename = "R:/Arshan Abbas/Image_overlay/Images/W4-1-S1-NEU.jpg"
print("Reading img 2:", refFilename)
im2 = cv2.imread(imFilename, cv2.IMREAD_COLOR)
im2 = cv2.cvtColor(im2, cv2.COLOR_BGR2RBG)

#Display Image

plt.figure(figsize=[20,10]);
plt.subplot(121); plt.axis('off'); plt.imshow(im1), plt.title("Original")
plt.subplot(122); plt.axis('off'); plt.imshow(im2), plt.title("Scanned")

#Convert to grayscale
im1_gray = cv2.cvtColor(im1, cv2.COLOR_BGR2GRAY)
im2_gray = cv2.cvtColor(im2, cv2.COLOR_BGR2GRAY)

#Detect ORB features
MAX_NUM_FEATURES = 500
orb = cv2.ORB_create(MAX_NUM_FEATURES)
keypoints1, descriptors1 = orb.detectAndCompute(im1_gray, None)
keypoints2, descriptors2 = orb.detectAndCompute(im2_gray, None)

#Display
im1_display = cv2.drawKeypoints(im1, keypoints1, outImage=np.array([]), color=(255,0,0), flags=cv2.draw_matches_flags_draw_rich_keypoints)
im2_display = cv2.drawKeypoints(im2, keypoints2, outImage=np.array([]), color=(255,0,0), flags=cv2.draw_matches_flags_draw_rich_keypoints)

#match features
matcher = cv2.DescriptorMatcher_create(cv2.DESCRIPTOR_MATCHER_BRUTEFORCE_HAMMING)
matches = matcher.match(descriptorsl, descriptors2, None)

#Sort matches
matches.sort(key=lamda x: x.distance, reverse=False)

#Remove not good matches
numGoodMatches = int(len(matches) * 0.1)
matches = matches[:numGoodMatches]

#Draw top matches
im_matches = cv2.drawMatches(im1, keypointsl, im2, keypoints2, matches, None)

plt.figure(figsize=[40,10])
plt.imshow(im_matches); plt.axis('off'), plt.title("Original Form");

#Find Homography
points1 = np.zeros((len(matches), 2), dtype=np.float32)
points2 = np.zeros((len(matches), 2), dtype=np.float32)

for i, match in enumerate(matches):
    points1[i, :] = keypoints1[match.queryIdx].pt
    points2[i, :] = keypoints2[match.queryIdx].pt

#Find homography
h, mask = cv2.findHomography(point2, point1, cv2.RANSAC)

#Use homography to wrap image
height, width, channels = im1.shape
im2_reg = cv2.warpPerspective(im2, h, (width, height))

#Dispaly results
plt.figure(figsize=[20,10]);
plt.subplot(121); plt.imshow(im1); plt.axis('off'); plt.title("Original");
plt.subplot(122); plt.imshow(im2_reg); plt.axis('off'); plt.title("Scanned");