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

# Define folders to save original and pencil sketch-filtered images
filtered_folder = 'filtered'  # Base folder for filtered images
sketch_folder = os.path.join(filtered_folder, 'sketch')  # Folder for pencil sketch-filtered images

# Ensure folders exist before saving images. If they don't exist, they will be created to avoid file errors.
for folder in [filtered_folder, sketch_folder]:
    if not os.path.exists(folder):
        os.makedirs(folder)  # Creates the folder if it doesn't exist
        print(f"Folder created: {folder}")  # Print the folder creation confirmation
    else:
        print(f"Folder already exists: {folder}")  # Print if the folder already exists

# Load images from the base path specified in the config file.
# cv2.imread reads an image from a file and returns a NumPy array.
flower = cv2.imread(os.path.join(image_path, 'Flowers.jpg'))
santorini = cv2.imread(os.path.join(image_path, 'Santorini.jpg'))

# Check if the images are loaded successfully
if flower is None or santorini is None:
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
    plt.imshow(cv2.cvtColor(img2, cv2.COLOR_BGR2RGB) if len(img2.shape) == 3 else img2, cmap='gray')  # Display grayscale if needed
    plt.axis('off')  # Hide axis for cleaner display
    plt.title(title2)  # Add a title for the filtered image

    plt.show()  # Display the figure

# Apply pencil sketch filter (black and white) to the 'flower' image
def pencil_sketch_bw(img):
    """
    Apply a pencil sketch effect (black and white) to the input image.
    :param img: Input image
    :return: Black-and-white pencil sketch image
    """
    img_blur = cv2.GaussianBlur(img, (5, 5), 0)  # Apply Gaussian blur
    img_sketch_bw, _ = cv2.pencilSketch(img_blur)  # Get the black-and-white sketch
    return img_sketch_bw  # Return the black-and-white sketch image

# Apply pencil sketch filter (black and white + color) to the 'santorini' image
def pencil_sketch_bw_color(img):
    """
    Apply a pencil sketch effect (both black and white and color) to the input image.
    :param img: Input image
    :return: Tuple of black-and-white sketch and color sketch images
    """
    img_blur = cv2.GaussianBlur(img, (5, 5), 0)  # Apply Gaussian blur
    img_sketch_bw, img_sketch_color = cv2.pencilSketch(img_blur)  # Get both black-and-white and color sketches
    return img_sketch_bw, img_sketch_color  # Return both sketch versions

# Process the 'flower' image and display the black-and-white sketch
img_sketch_flower_bw = pencil_sketch_bw(flower)
plot(flower, img_sketch_flower_bw, "Original Image (Flower)", "Pencil Sketch (BW)")

# Save the black-and-white pencil sketch of the flower image
sketch_flower_bw_path = os.path.join(sketch_folder, 'Flower_sketch_bw.jpg')
cv2.imwrite(sketch_flower_bw_path, img_sketch_flower_bw)  # Save black-and-white sketch
print(f"Black-and-white pencil sketch of flower saved at: {sketch_flower_bw_path}")

# Process the 'santorini' image and display both black-and-white and color sketches
img_sketch_santorini_bw, img_sketch_santorini_color = pencil_sketch_bw_color(santorini)
plot(santorini, img_sketch_santorini_bw, "Original Image (Santorini)", "Pencil Sketch (BW)")

# Save the black-and-white pencil sketch of the santorini image
sketch_santorini_bw_path = os.path.join(sketch_folder, 'Santorini_sketch_bw.jpg')
cv2.imwrite(sketch_santorini_bw_path, img_sketch_santorini_bw)  # Save black-and-white sketch
print(f"Black-and-white pencil sketch of santorini saved at: {sketch_santorini_bw_path}")

# Save the color pencil sketch of the santorini image
sketch_santorini_color_path = os.path.join(sketch_folder, 'Santorini_sketch_color.jpg')
cv2.imwrite(sketch_santorini_color_path, img_sketch_santorini_color)  # Save color sketch
print(f"Color pencil sketch of santorini saved at: {sketch_santorini_color_path}")
