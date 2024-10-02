import cv2
import numpy as np
import matplotlib.pyplot as plt
import os
import json
import matplotlib  # Import matplotlib to set the backend for displaying images

# Ensure Matplotlib uses an interactive backend for displaying images
matplotlib.use('TkAgg')

# Load configuration from the 'config.json' file, which contains important settings such as image paths
with open('/Users/arinzemomife/Photoshop-Filters-Showcase/config.json') as config_file:
    config = json.load(config_file)

# Get the image path from the config file. This helps to dynamically set the location of images.
image_path = config.get('image_path')

# Raise an error if the image path is not found in the config file, ensuring the script doesn't proceed with invalid data.
if not image_path:
    raise ValueError("Image path not found in configuration file.")

# Define folders to save original and brightness-improved images
filtered_folder = 'filtered'  # Base folder for filtered images
original_folder = os.path.join(filtered_folder, 'originals')  # Folder for original images
brightness_folder = os.path.join(filtered_folder, 'brightness')  # Folder for brightness-improved images

# Ensure folders exist before saving images. If they don't exist, they will be created to avoid file errors.
for folder in [filtered_folder, original_folder, brightness_folder]:
    if not os.path.exists(folder):
        os.makedirs(folder)  # Creates the folder if it doesn't exist
        print(f"Folder created: {folder}")  # Print the folder creation confirmation
    else:
        print(f"Folder already exists: {folder}")  # Print if the folder already exists

# Load images from the base path specified in the config file.
# cv2.imread reads an image from a file and returns a NumPy array.
monument = cv2.imread(os.path.join(image_path, 'Monument.jpg'))

# Check if the image is loaded successfully
if monument is None:
    print("Error: Image could not be loaded. Check the file path.")
else:
    print("Image loaded successfully!")  # Confirmation message that image is loaded

# Define the plot function to display two images side by side for comparison (original vs filtered)
def plot(img1, img2, title1="Original Image", title2="Filtered Image"):
    """
    Display two images side by side using Matplotlib for easy comparison.
    :param img1: First image (original)
    :param img2: Second image (filtered)
    :param title1: Title for the first image
    :param title2: Title for the second image
    """
    fig = plt.figure(figsize=(20, 10))  # Create a figure of specified size for better visualization

    # Display the first image (original)
    plt.subplot(1, 2, 1)  # 1 row, 2 columns, position 1 for the original image
    plt.imshow(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))  # Convert BGR (OpenCV) to RGB (Matplotlib) for correct colors
    plt.axis('off')  # Hide axis for a cleaner display
    plt.title(title1)  # Add a title to the original image

    # Display the second image (filtered)
    plt.subplot(1, 2, 2)  # 1 row, 2 columns, position 2 for the filtered image
    plt.imshow(cv2.cvtColor(img2, cv2.COLOR_BGR2RGB))  # Convert BGR (OpenCV) to RGB for correct display
    plt.axis('off')  # Hide axis for cleaner display
    plt.title(title2)  # Add a title for the filtered image

    plt.show()  # Display the figure

# Define function for improving brightness
def bright(img, level):
    """
    Improve the brightness of an image using cv2.convertScaleAbs().
    :param img: Input image
    :param level: Brightness adjustment level
    :return: Image with improved brightness
    """
    img_bright = cv2.convertScaleAbs(img, beta=level)  # Adjust brightness using the 'beta' parameter
    return img_bright  # Return the brightness-adjusted image

# Apply brightness improvement to the 'monument' image
img_bright = bright(monument, 25)

# Display the original and brightness-improved image side by side
plot(monument, img_bright, "Original Image", "Brightness Improved")

# Save the brightness-improved image
bright_image_path = os.path.join(brightness_folder, 'Monument_bright.jpg')
cv2.imwrite(bright_image_path, img_bright)  # Save brightness-improved image
print(f"Brightness improved image saved at: {bright_image_path}")
