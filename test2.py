import cv2
import numpy as np

# Define your feature points
features_image1 = [(2116, 1673), (2102, 2999), (15850, 1424), (15910, 2999)]
features_image2 = [(2794, 1689), (2799, 2999), (16527, 1211), (16614, 2999)]

# Convert feature points to numpy arrays
points1 = np.array(features_image1, dtype=np.float32)
points2 = np.array(features_image2, dtype=np.float32)

# Estimate affine transformation matrix
transformation_matrix, _ = cv2.estimateAffinePartial2D(points1, points2)

print("Transformation Matrix:")
print(transformation_matrix)