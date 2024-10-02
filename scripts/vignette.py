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

#Define function for Vignette filter
def vignette(img, level = 2):
    
    height, width = img.shape[:2]  
    
    # Generate vignette mask using Gaussian kernels.
    X_resultant_kernel = cv2.getGaussianKernel(width, width/level)
    Y_resultant_kernel = cv2.getGaussianKernel(height, height/level)
        
    # Generating resultant_kernel matrix.
    kernel = Y_resultant_kernel * X_resultant_kernel.T 
    mask = kernel / kernel.max()
    
    img_vignette = np.copy(img)
        
    # Applying the mask to each channel in the input image.
    for i in range(3):
        img_vignette[:,:,i] = img_vignette[:,:,i] * mask
    
    return img_vignette

img = flower
img_vignette = vignette(img)
plot(img, img_vignette)

plt.show()  # Display the figure