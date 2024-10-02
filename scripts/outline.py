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

# Define folders to save original and outline-filtered images
filtered_folder = 'filtered'  # Base folder for filtered images
original_folder = os.path.join(filtered_folder, 'originals')  # Folder for original images
outline_folder = os.path.join(filtered_folder, 'outline')  # Folder for outline-filtered images

# Ensure folders exist before saving images. If they don't exist, they will be created to avoid file errors.
for folder in [filtered_folder, original_folder, outline_folder]:
    if not os.path.exists(folder):
        os.makedirs(folder)  # Creates the folder if it doesn't exist
        print(f"Folder created: {folder}")  # Print the folder creation confirmation
    else:
        print(f"Folder already exists: {folder}")  # Print if the folder already exists

# Load images from the base path specified in the config file.
# cv2.imread reads an image from a file and returns a NumPy array.
monument = cv2.imread(os.path.join(image_path, 'Monument.jpg'))
house = cv2.imread(os.path.join(image_path, 'House.jpg'))

# Check if the images are loaded successfully
if monument is None or house is None:
    print("Error: One or more images could not be loaded. Check the file paths.")
else:
    print("Images loaded successfully!")  # Confirmation message that images are loaded

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

# Define function for applying outline filter
def outline(img, k=9):
    """
    Apply an outline filter to the image using a custom kernel to detect edges.
    :param img: Input image
    :param k: Kernel intensity for edge detection (default is 9)
    :return: Image with outline effect
    """
    k = max(k, 9)  # Ensure the kernel value is at least 9
    kernel = np.array([[-1, -1, -1],  # Custom kernel for outlining
                       [-1,  k, -1],
                       [-1, -1, -1]])

    # Apply the outline filter using filter2D
    img_outline = cv2.filter2D(img, ddepth=-1, kernel=kernel)
    return img_outline  # Return the outline-filtered image

# Define function for black-and-white filter
def bw_filter(img):
    """
    Convert the input image to grayscale (black and white).
    :param img: Input image
    :return: Grayscale image
    """
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply outline filter to the 'monument' image with kernel = 10
img_outline_monument = outline(monument, k=10)
plot(monument, img_outline_monument, "Original Image", "Outline Image")

# Save the outline-filtered image of monument
outline_monument_path = os.path.join(outline_folder, 'Monument_outline.jpg')
cv2.imwrite(outline_monument_path, img_outline_monument)  # Save outline-filtered image
print(f"Outline image saved at: {outline_monument_path}")

# Apply black-and-white filter and then outline filter to the 'monument' image
img_bw_monument = bw_filter(monument)
img_bw_outline_monument = outline(img_bw_monument, k=10)
plot(img_bw_monument, img_bw_outline_monument, "Black and White Image", "Outline Image")

# Save the black-and-white outline-filtered image of monument
outline_bw_monument_path = os.path.join(outline_folder, 'Monument_bw_outline.jpg')
cv2.imwrite(outline_bw_monument_path, img_bw_outline_monument)  # Save black-and-white outline-filtered image
print(f"Black-and-white outline image saved at: {outline_bw_monument_path}")

# Apply outline filter to the 'house' image with kernel = 10
img_outline_house = outline(house, k=10)
plot(house, img_outline_house, "Original Image", "Outline Image")

# Save the outline-filtered image of house
outline_house_path = os.path.join(outline_folder, 'House_outline.jpg')
cv2.imwrite(outline_house_path, img_outline_house)  # Save outline-filtered image
print(f"Outline image saved at: {outline_house_path}")
