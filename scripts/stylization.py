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

# Define folders to save original and stylization-filtered images
filtered_folder = 'filtered'  # Base folder for filtered images
stylization_folder = os.path.join(filtered_folder, 'stylization')  # Folder for stylization-filtered images

# Ensure folders exist before saving images. If they don't exist, they will be created to avoid file errors.
for folder in [filtered_folder, stylization_folder]:
    if not os.path.exists(folder):
        os.makedirs(folder)  # Creates the folder if it doesn't exist
        print(f"Folder created: {folder}")  # Print the folder creation confirmation
    else:
        print(f"Folder already exists: {folder}")  # Print if the folder already exists

# Load the santorini image from the base path specified in the config file.
santorini = cv2.imread(os.path.join(image_path, 'Santorini.jpg'))

# Check if the image is loaded successfully
if santorini is None:
    print("Error: Santorini image could not be loaded. Check the file path.")
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

# Apply the stylization filter to the 'santorini' image
def stylization_filter(img, sigma_s=40, sigma_r=0.1):
    """
    Apply a stylization filter to the input image using OpenCV's stylization method.
    :param img: Input image
    :param sigma_s: Controls the size of the texture (default is 40)
    :param sigma_r: Controls how much of the color is preserved (default is 0.1)
    :return: Stylized image
    """
    img_blur = cv2.GaussianBlur(img, (5, 5), 0)  # Apply Gaussian blur to reduce noise
    img_style = cv2.stylization(img_blur, sigma_s=sigma_s, sigma_r=sigma_r)  # Apply stylization filter
    return img_style  # Return the stylized image

# Apply the stylization filter to the santorini image
img_stylized = stylization_filter(santorini)
plot(santorini, img_stylized, "Original Image (Santorini)", "Stylized Image")

# Save the stylized image
stylization_image_path = os.path.join(stylization_folder, 'Santorini_stylized.jpg')
cv2.imwrite(stylization_image_path, img_stylized)  # Save stylized image
print(f"Stylized image of santorini saved at: {stylization_image_path}")
