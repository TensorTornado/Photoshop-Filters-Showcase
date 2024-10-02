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

# Define folders to save original, black and white, sepia, and edge detection filtered images
filtered_folder = 'filtered'  # Base folder for filtered images
original_folder = os.path.join(filtered_folder, 'originals')  # Folder for original images
edge_folder = os.path.join(filtered_folder, 'edges')  # New folder for edge detection filtered images

# Ensure folders exist before saving images. If they don't exist, they will be created to avoid file errors.
for folder in [filtered_folder, original_folder, edge_folder]:
    if not os.path.exists(folder):
        os.makedirs(folder)  # Creates the folder if it doesn't exist
        print(f"Folder created: {folder}")  # Print the folder creation confirmation
    else:
        print(f"Folder already exists: {folder}")  # Print if the folder already exists

# Load images from the base path specified in the config file.
# cv2.imread reads an image from a file and returns a NumPy array.
coast = cv2.imread(os.path.join(image_path, 'California_Coast.jpg'))

# Check if the image is loaded successfully
if coast is None:
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
    plt.imshow(img2, cmap='gray')  # Display the edges in grayscale
    plt.axis('off')  # Hide axis for cleaner display
    plt.title(title2)  # Add a title for the filtered image

    plt.show()  # Display the figure

# Define function for applying Canny edge detection
def edge_detection(img, apply_blur=False):
    """
    Perform edge detection on an image using the Canny method.
    :param img: Input image
    :param apply_blur: Apply Gaussian blur before edge detection (default is False)
    :return: Image with detected edges
    """
    if apply_blur:
        # Apply Gaussian blur to reduce noise before edge detection
        img = cv2.GaussianBlur(img, (5, 5), 0)

    # Perform Canny edge detection
    img_edges = cv2.Canny(img, 100, 200)

    return img_edges  # Return the edge-detected image

# Apply edge detection without blur
img_edges = edge_detection(coast)
plot(coast, img_edges, "Original Image", "Edges without Blur")

# Apply edge detection with Gaussian blur
img_edges_blur = edge_detection(coast, apply_blur=True)
plot(coast, img_edges_blur, "Original Image", "Edges with Blur")

# Save the edge detection images
edge_image_path = os.path.join(edge_folder, 'California_Coast_edges.jpg')
cv2.imwrite(edge_image_path, img_edges)  # Save edge-detected image without blur
print(f"Edge detection image saved at: {edge_image_path}")

edge_blur_image_path = os.path.join(edge_folder, 'California_Coast_edges_blur.jpg')
cv2.imwrite(edge_blur_image_path, img_edges_blur)  # Save edge-detected image with blur
print(f"Edge detection image with blur saved at: {edge_blur_image_path}")
