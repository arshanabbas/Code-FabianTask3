import cv2
import numpy as np

# Load the reference and target images
reference_image = cv2.imread("R:/Arshan Abbas/Image_overlay/Images/W4-1-S1-NEU.jpg", cv2.IMREAD_GRAYSCALE)
target_image = cv2.imread("R:/Arshan Abbas/Image_overlay/Images/W4-1-S1-Kalling2-NEU.jpg", cv2.IMREAD_GRAYSCALE)
#3 "R:/Arshan Abbas/Image_overlay/Images/W4-1-S1-Kalling2-NEU.jpg" "R:/Arshan Abbas/Image_overlay/Images/W4-1-S1-NEU.jpg"

# Find keypoints and descriptors using ORB (you can use other methods like SIFT, SURF, etc.)
orb = cv2.ORB_create()
kp1, des1 = orb.detectAndCompute(reference_image, None)
kp2, des2 = orb.detectAndCompute(target_image, None)

# Create a brute-force matcher
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

# Match the descriptors
matches = bf.match(des1, des2)

# Sort the matches by distance
matches = sorted(matches, key=lambda x: x.distance)

# Keep only the best N matches
N = 10
matches = matches[:N]

# Extract matched keypoints
src_pts = np.float32([kp1[m.queryIdx].pt for m in matches]).reshape(-1, 1, 2)
dst_pts = np.float32([kp2[m.trainIdx].pt for m in matches]).reshape(-1, 1, 2)

# Compute the transformation matrix using RANSAC
M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)

# Apply the transformation to the target image
registered_image = cv2.warpPerspective(target_image, M, (reference_image.shape[1], reference_image.shape[0]))

# Save the registered image
cv2.imwrite("R:/Arshan Abbas/Image_overlay/Images/registered_image3.jpg", registered_image)

# Display the registered image
#cv2.imshow(‘Registered Image’, registered_image)
cv2.waitKey(0)
cv2.destroyAllWindows()