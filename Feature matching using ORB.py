# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 11:49:20 2024

@author: arab
"""

import numpy as np 
import cv2 
   
      
# Read the query image as query_img 
# and train image This query image 
# is what you need to find in train image 
# Save it in the same directory 
# with the name image.jpg   
query_img = cv2.imread("R:/Arshan Abbas/Image_overlay/Images/W4-1-S1-Kalling2-NEU.jpg") 
train_img = cv2.imread("R:/Arshan Abbas/Image_overlay/Images/W4-1-S1-NEU.jpg") 
   
# Convert it to grayscale 
query_img_bw = cv2.cvtColor(query_img,cv2.COLOR_BGR2GRAY) 
train_img_bw = cv2.cvtColor(train_img, cv2.COLOR_BGR2GRAY) 
   
# Initialize the ORB detector algorithm 
orb = cv2.ORB_create() 
   
# Now detect the keypoints and compute 
# the descriptors for the query image 
# and train image 
queryKeypoints, queryDescriptors = orb.detectAndCompute(query_img_bw,None) 
trainKeypoints, trainDescriptors = orb.detectAndCompute(train_img_bw,None) 
  
# Initialize the Matcher for matching 
# the keypoints and then match the 
# keypoints 
matcher = cv2.BFMatcher() 
matches = matcher.match(queryDescriptors,trainDescriptors) 
   
# draw the matches to the final image 
# containing both the images the drawMatches() 
# function takes both images and keypoints 
# and outputs the matched query image with 
# its train image 
final_img = cv2.drawMatches(query_img, queryKeypoints,  
train_img, trainKeypoints, matches[:20],None) 
   
final_img = cv2.resize(final_img, (1000,650)) 
  
# Save the registered image
cv.imwrite("R:/Arshan Abbas/Image_overlay/Images/registered_image5.jpg", final_img)