from PIL import Image
import numpy as np

# Load the image
image = Image.open('G:/F/Work/TIME/Script/Code-Fabian3/1.jpg')  

# Define the ranges for x-axis and y-axis
x_start, x_end = 2090, 2100
y_start, y_end = 1675, -1  

# Crop the image to the specified portion
cropped_image = image.crop((x_start, y_start, x_end, y_end))

# Convert the cropped image to a NumPy array
cropped_array = np.array(cropped_image)

# Mask to select pixel values greater than 100 on the x-axis
mask = cropped_array[:, :, 0] > 100  # Assuming it's a grayscale image, accessing the first channel

# Apply the mask to select pixel values greater than 100
selected_pixels = cropped_array[mask]

# Print the selected pixel values
print(selected_pixels)



