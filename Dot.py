import cv2
import numpy as np

# Load the image
image = cv2.imread('G:/F/Work/TIME/Script/Code-Fabian3/1.jpg')

# Define the position for the red dot
x_pos1, y_pos1 = 2097, 2000  
x_pos2, y_pos2 = 2096, 2020  
x_pos3, y_pos3 = 2096, 2100  
x_pos4, y_pos4 = 2095, 2150  
x_pos5, y_pos5 = 2096, 2350  

# Draw a red dot on the image
cv2.circle(image, (x_pos1, y_pos1), 1, (0, 0, 255), -1)  
cv2.circle(image, (x_pos2, y_pos2), 1, (0, 0, 255), -1)  
cv2.circle(image, (x_pos3, y_pos3), 1, (0, 0, 255), -1)  
cv2.circle(image, (x_pos4, y_pos4), 1, (0, 0, 255), -1)  
cv2.circle(image, (x_pos5, y_pos5), 1, (0, 0, 255), -1)  

# Display the image (optional)
cv2.imwrite('G:/F/Work/TIME/Script/Code-Fabian3/ModifiedImage.jpg', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
