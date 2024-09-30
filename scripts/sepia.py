import cv2
import numpy as np
import matplotlib.pyplot as plt
import os
import json
import matplotlib  # Import matplotlib to set the backend

# Ensure Matplotlib uses an interactive backend for displaying images
matplotlib.use('TkAgg')

# Load configuration from the 'config.json' file
with open('/Users/arinzemomife/Photoshop-Filters-Showcase/config.json') as config_file:
    config = json.load(config_file)

# Get the image path from the config file
image_path = config.get('image_path')

# Raise an error if the image path is not found in the config file
if not image_path:
    raise ValueError("Image path not found in configuration file.")

# Define folders to save original, black and white, and sepia filtered images
original_folder = os.path.join('filtered', 'originals')
bw_folder = os.path.join('filtered', 'black_and_white')
sepia_folder = os.path.join('filtered', 'sepia')  # New folder for sepia images

# Ensure folders exist before saving images
for folder in [original_folder, bw_folder, sepia_folder]:
    if not os.path.exists(folder):
        os.makedirs(folder)  # Create the folder if it doesn't exist

# Load images from the base path specified in the config file
flower = cv2.imread(os.path.join(image_path, 'Flowers.jpg'))
house = cv2.imread(os.path.join(image_path, 'House.jpg'))
monument = cv2.imread(os.path.join(image_path, 'Monument.jpg'))
santorini = cv2.imread(os.path.join(image_path, 'Santorini.jpg'))
new_york = cv2.imread(os.path.join(image_path, 'New_York.jpg'))
coast = cv2.imread(os.path.join(image_path, 'California_Coast.jpg'))

# Check if all images are loaded successfully
if any(img is None for img in [flower, house, monument, santorini, new_york, coast]):
    print("Error: One or more sample images could not be loaded. Check the file paths.")
else:
    print("All images loaded successfully!")

# Define the plot function to display two images side by side
def plot(img1, img2):
    """
    Display two images side by side using Matplotlib.
    :param img1: First image (original)
    :param img2: Second image (filtered)
    """
    fig = plt.figure(figsize=(20, 10))  # Create a figure of specified size

    # Display the first image (original)
    plt.subplot(1, 2, 1)  # 1 row, 2 columns, position 1
    plt.imshow(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))  # Convert BGR to RGB for Matplotlib
    plt.axis('off')  # Hide axis for cleaner display
    plt.title("Original Image")  # Title for the original image

    # Display the second image (filtered)
    plt.subplot(1, 2, 2)  # 1 row, 2 columns, position 2
    plt.imshow(cv2.cvtColor(img2, cv2.COLOR_BGR2RGB))  # Convert BGR to RGB for Matplotlib
    plt.axis('off')  # Hide axis for cleaner display
    plt.title("Filtered Image")  # Title for the filtered image

    plt.show()  # Display the figure

# Define the sepia filter function
def sepia(img):
    """
    Apply a sepia filter to the given image.
    :param img: Input image (BGR format)
    :return: Sepia-toned image (BGR format)
    """
    img_sepia = img.copy()  # Make a copy of the original image to avoid changing it directly
    
    # Convert the image to RGB because the sepia matrix is designed for RGB
    img_sepia = cv2.cvtColor(img_sepia, cv2.COLOR_BGR2RGB)

    # Convert to float to handle matrix multiplication properly
    img_sepia = np.array(img_sepia, dtype=np.float64)

    # Apply the sepia transformation matrix to the image
    img_sepia = cv2.transform(img_sepia, np.matrix([[0.393, 0.769, 0.189],
                                                    [0.349, 0.686, 0.168],
                                                    [0.272, 0.534, 0.131]]))

    # Clip the pixel values to ensure they remain in the range [0, 255]
    img_sepia = np.clip(img_sepia, 0, 255)
    
    # Convert back to uint8 (standard image format) after applying the filter
    img_sepia = np.array(img_sepia, dtype=np.uint8)

    # Convert the image back to BGR format because OpenCV uses BGR by default
    img_sepia = cv2.cvtColor(img_sepia, cv2.COLOR_RGB2BGR)
    
    return img_sepia  # Return the sepia-toned image

# Apply the sepia filter to the flower image
img = flower  # Assign the flower image to the variable 'img'
img_sepia = sepia(img)  # Apply the sepia filter to the image

# Display the original and sepia images side by side using the plot function
plot(img, img_sepia)

# Save the sepia filtered image to the sepia folder
sepia_output_path = os.path.join(sepia_folder, 'flower_sepia.jpg')
cv2.imwrite(sepia_output_path, img_sepia)  # Corrected from 'flower_sepia' to 'img_sepia'
print(f"Sepia image saved at: {sepia_output_path}")  # Confirm that the image was saved

# Optionally, display the sepia image using matplotlib
plt.imshow(cv2.cvtColor(img_sepia, cv2.COLOR_BGR2RGB))  # Convert BGR to RGB for correct display
plt.title("Sepia Filter Applied")
plt.show()  # Display the sepia image
