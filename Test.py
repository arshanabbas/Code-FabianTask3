import cv2
import numpy as np

# Load images
image1 = cv2.imread('1.jpg', cv2.IMREAD_GRAYSCALE)
image2 = cv2.imread('2.jpg', cv2.IMREAD_GRAYSCALE)

# Define your feature points
features_image1 = [(2116, 1673), (2115, 1674), (2115, 1675), (2114, 1676), (2114, 1677), (2113, 1678), (2113, 1679), (2112, 1680), (2112, 1681), (2111, 1682), 
                   (2101, 2990), (2101, 2991), (2102, 2992), (2101, 2993), (2101, 2994), (2101, 2995), (2101, 2996), (2101, 2997), (2102, 2998), (2102, 2999), 
                   (15850, 1424), (15841, 1433), (15866, 1434), (15869, 1435), (15871, 1436), (15872, 1437), (15872, 1438), (15872, 1439), (15872, 1440), (15872, 1441), 
                   (15910, 2990), (15910, 2991), (15910, 2992), (15910, 2993), (15910, 2994), (15910, 2995), (15910, 2996), (15910, 2997), (15910, 2998), (15910, 2999)]
features_image2 = [(2794, 1689), (2791, 1690), (2790, 1691), (2790, 1692), (2789, 1693), (2789, 1694), (2789, 1695), (2788, 1696), (2787, 1697), (2787, 1698), 
                   (2799, 2990), (2799, 2991), (2799, 2992), (2799, 2993), (2799, 2994), (2799, 2995), (2799, 2996), (2799, 2997), (2799, 2998), (2799, 2999), 
                   (16527, 1211), (16537, 1212), (16539, 1213), (16540, 1214), (16540, 1215), (16541, 1216), (16541, 1217), (16541, 1218), (16541, 1219), (16541, 1220), 
                   (16614, 2990), (16615, 2991), (16615, 2992), (16614, 2993), (16613, 2994), (16613, 2995), (16614, 2996), (16614, 2997), (16614, 2998), (16614, 2999)]

# Convert feature points to numpy arrays
points1 = np.array(features_image1, dtype=np.float32)
points2 = np.array(features_image2, dtype=np.float32)

# Estimate transformation matrix (e.g., using RANSAC)
transformation_matrix, _ = cv2.estimateAffine2D(points1, points2)

# Warp image1 to align with image2
aligned_image1 = cv2.warpAffine(image2, transformation_matrix, (image1.shape[1], image1.shape[0]))

combined_image = cv2.addWeighted(image1, 0.6, aligned_image1, 0.6, 0)

#results
cv2.imwrite('wrappedIMG.jpg', combined_image)
print(transformation_matrix)