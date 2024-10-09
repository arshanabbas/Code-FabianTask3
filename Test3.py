import numpy as np
import cv2

# Define your feature points
features_image1 = [(2116, 1673), (2115, 1674), (2115, 1675), (2114, 1676), (2114, 1677), (2113, 1678), (2113, 1679), (2112, 1680), (2112, 1681), (2111, 1682),
                   (2101, 2990), (2101, 2991), (2102, 2992), (2101, 2993), (2101, 2994), (2101, 2995), (2101, 2996), (2101, 2997), (2102, 2998), (2102, 2999),
                   (2116, 1671), (2117, 1671), (2118, 1671), (2119, 1671), (2120, 1671), (2121, 1671), (2122, 1672), (2123, 1671), (2124, 1671), (2125, 1671),
                   (15840, 1417), (15841, 1417), (15842, 1418), (15843, 1420), (15844, 1430), (15845, 1430), (15846, 1424), (15847, 1423), (15848, 1422), (15849, 1422),
                   (15850, 1424), (15841, 1433), (15866, 1434), (15869, 1435), (15871, 1436), (15872, 1437), (15872, 1438), (15872, 1439), (15872, 1440), (15872, 1441),
                   (15910, 2990), (15910, 2991), (15910, 2992), (15910, 2993), (15910, 2994), (15910, 2995), (15910, 2996), (15910, 2997), (15910, 2998), (15910, 2999)]
features_image2 = [(2794, 1689), (2791, 1690), (2790, 1691), (2790, 1692), (2789, 1693), (2789, 1694), (2789, 1695), (2788, 1696), (2787, 1697), (2787, 1698),
                   (2799, 2990), (2799, 2991), (2799, 2992), (2799, 2993), (2799, 2994), (2799, 2995), (2799, 2996), (2799, 2997), (2799, 2998), (2799, 2999),
                   (2794, 1686), (2795, 1687), (2796, 1687), (2797, 1688), (2798, 1688), (2799, 1687), (2895, 1688), (2896, 1688), (2897, 1688), (2898, 1687),
                   (16517, 1192), (16518, 1192), (16519, 1193), (16520, 1193), (16521, 1193), (16522, 1194), (16523, 1195), (16524, 1199), (16525, 1212), (16526, 1211),
                   (16527, 1211), (16537, 1212), (16539, 1213), (16540, 1214), (16540, 1215), (16541, 1216), (16541, 1217), (16541, 1218), (16541, 1219), (16541, 1220),
                   (16614, 2990), (16615, 2991), (16615, 2992), (16614, 2993), (16613, 2994), (16613, 2995), (16614, 2996), (16614, 2997), (16614, 2998), (16614, 2999)]

# Verify that both feature lists have the same number of points
if len(features_image1) != len(features_image2):
    raise ValueError("The number of feature points in both images must be the same.")

# Convert feature points to NumPy arrays of shape (N, 1, 2) as required by OpenCV
pts_image1 = np.array(features_image1, dtype=np.float32).reshape(-1, 1, 2)
pts_image2 = np.array(features_image2, dtype=np.float32).reshape(-1, 1, 2)

# Optionally, visualize the correspondences to ensure they are correct
def draw_correspondences(img1, img2, pts1, pts2):
    # Concatenate images side by side
    combined_img = np.hstack((img1, img2))
    # Adjust points from img2 to the concatenated image
    pts2_adjusted = pts2.copy()
    pts2_adjusted[:, 0, 0] += img1.shape[1]  # Shift x-coordinates by width of img1

    for p1, p2 in zip(pts1, pts2_adjusted):
        p1 = tuple(p1.ravel().astype(int))
        p2 = tuple(p2.ravel().astype(int))
        cv2.circle(combined_img, p1, 5, (0, 255, 0), -1)
        cv2.circle(combined_img, p2, 5, (0, 255, 0), -1)
        cv2.line(combined_img, p1, p2, (255, 0, 0), 1)

# Load the images
image1_path = '1.jpg'  # Replace with your first image path
image2_path = '2.jpg'  # Replace with your second image path

image1 = cv2.imread(image1_path)
image2 = cv2.imread(image2_path)

if image1 is None:
    raise FileNotFoundError(f"Image1 not found at path: {image1_path}")
if image2 is None:
    raise FileNotFoundError(f"Image2 not found at path: {image2_path}")

# Optional: Visualize correspondences
# draw_correspondences(image1, image2, pts_image1, pts_image2)

# Compute homography matrix using RANSAC for robustness against outliers
homography_matrix, status = cv2.findHomography(pts_image2, pts_image1, cv2.RANSAC)

if homography_matrix is None:
    raise ValueError("Homography could not be computed. Check the feature correspondences.")

print("Homography Matrix:")
print(homography_matrix)

# Warp image2 to align with image1
height, width, channels = image1.shape  # Use image1 dimensions for the output

aligned_image2 = cv2.warpPerspective(image2, homography_matrix, (width, height))

# Save the aligned image
aligned_image_path = 'aligned_imagee.jpg'
cv2.imwrite(aligned_image_path, aligned_image2)
print(f"Aligned image saved as {aligned_image_path}")