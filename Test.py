import cv2
import numpy as np

# Load images
image1 = cv2.imread('1.jpg', cv2.IMREAD_GRAYSCALE)
image2 = cv2.imread('2.jpg', cv2.IMREAD_GRAYSCALE)

# Each point should be in the format (x, y)
features_image1 = [(2116, 1673), (2102, 2999), (15850, 1424), (15910, 2999)]
features_image2 = [(2794, 1689), (2799, 2999), (16527, 1211), (16614, 2999)]

# Convert feature points to numpy arrays
points1 = np.array(features_image1, dtype=np.float32)
points2 = np.array(features_image2, dtype=np.float32)

# Estimate transformation matrix (e.g., using RANSAC)
transformation_matrix, _ = cv2.estimateAffine2D(points1, points2)

# Warp image1 to align with image2
aligned_image1 = cv2.warpAffine(image1, transformation_matrix, (image1.shape[1], image1.shape[0]))

#results
cv2.imwrite('Aligned Image 1.jpg', aligned_image1)
cv2.imwrite('Image 2.jpg', image2)