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

# Define folders to save original and embossed images
filtered_folder = 'filtered'  # Base folder for filtered images
original_folder = os.path.join(filtered_folder, 'originals')  # Folder for original images
emboss_folder = os.path.join(filtered_folder, 'emboss')  # Folder for embossed edge images

# Ensure folders exist before saving images. If they don't exist, they will be created to avoid file errors.
for folder in [filtered_folder, original_folder, emboss_folder]:
    if not os.path.exists(folder):
        os.makedirs(folder)  # Creates the folder if it doesn't exist
        print(f"Folder created: {folder}")  # Print the folder creation confirmation
    else:
        print(f"Folder already exists: {folder}")  # Print if the folder already exists

# Load images from the base path specified in the config file.
# cv2.imread reads an image from a file and returns a NumPy array.
house = cv2.imread(os.path.join(image_path, 'House.jpg'))

# Check if the image is loaded successfully
if house is None:
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

# Define function for applying embossed edge detection
def embossed_edges(img):
    """
    Apply an emboss filter to the image using a custom kernel to highlight edges with an embossed effect.
    :param img: Input image
    :return: Image with embossed effect
    """
    kernel = np.array([[0, -3, -3],  # Custom kernel for embossing
                       [3,  0, -3], 
                       [3,  3,  0]])

    # Apply the embossing filter using filter2D
    img_emboss = cv2.filter2D(img, -1, kernel=kernel)
    return img_emboss  # Return the embossed image

# Apply embossed edge detection to the 'house' image
img_emboss = embossed_edges(house)

# Display the original and embossed image side by side
plot(house, img_emboss, "Original Image", "Embossed Edges")

# Save the embossed image
emboss_image_path = os.path.join(emboss_folder, 'House_emboss.jpg')
cv2.imwrite(emboss_image_path, img_emboss)  # Save embossed image
print(f"Embossed edge image saved at: {emboss_image_path}")
