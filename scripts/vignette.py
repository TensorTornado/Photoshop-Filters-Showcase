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

# Define folders to save original, black and white, sepia, and vignette filtered images
filtered_folder = 'filtered'  # Base folder for filtered images
original_folder = os.path.join(filtered_folder, 'originals')  # Folder for original images
bw_folder = os.path.join(filtered_folder, 'black_and_white')  # Folder for black and white filtered images
sepia_folder = os.path.join(filtered_folder, 'sepia')  # Folder for sepia filtered images
vignette_folder = os.path.join(filtered_folder, 'vignette')  # New folder for vignette filtered images

# Ensure folders exist before saving images. If they don't exist, they will be created to avoid file errors.
for folder in [filtered_folder, original_folder, bw_folder, sepia_folder, vignette_folder]:
    if not os.path.exists(folder):
        os.makedirs(folder)  # Creates the folder if it doesn't exist
        print(f"Folder created: {folder}")  # Print the folder creation confirmation
    else:
        print(f"Folder already exists: {folder}")  # Print if the folder already exists

# Load images from the base path specified in the config file.
# cv2.imread reads an image from a file and returns a NumPy array.
flower = cv2.imread(os.path.join(image_path, 'Flowers.jpg'))
house = cv2.imread(os.path.join(image_path, 'House.jpg'))
monument = cv2.imread(os.path.join(image_path, 'Monument.jpg'))
santorini = cv2.imread(os.path.join(image_path, 'Santorini.jpg'))
new_york = cv2.imread(os.path.join(image_path, 'New_York.jpg'))
coast = cv2.imread(os.path.join(image_path, 'California_Coast.jpg'))

# Check if all images are loaded successfully. If any of the images failed to load, print an error message.
if any(img is None for img in [flower, house, monument, santorini, new_york, coast]):
    print("Error: One or more sample images could not be loaded. Check the file paths.")
else:
    print("All images loaded successfully!")  # Confirmation message that all images are loaded

# Define the plot function to display two images side by side for comparison (original vs filtered)
def plot(img1, img2):
    """
    Display two images side by side using Matplotlib for easy comparison.
    :param img1: First image (original)
    :param img2: Second image (filtered)
    """
    fig = plt.figure(figsize=(20, 10))  # Create a figure of specified size for better visualization

    # Display the first image (original)
    plt.subplot(1, 2, 1)  # 1 row, 2 columns, position 1 for the original image
    plt.imshow(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))  # Convert BGR (OpenCV) to RGB (Matplotlib) for correct colors
    plt.axis('off')  # Hide axis for a cleaner display
    plt.title("Original Image")  # Add a title to the original image

    # Display the second image (filtered)
    plt.subplot(1, 2, 2)  # 1 row, 2 columns, position 2 for the filtered image
    plt.imshow(cv2.cvtColor(img2, cv2.COLOR_BGR2RGB))  # Convert BGR (OpenCV) to RGB for correct display
    plt.axis('off')  # Hide axis for cleaner display
    plt.title("Filtered Image")  # Add a title for the filtered image

    plt.show()  # Display the figure

# Define function for applying a vignette effect to the image
def vignette(img, level=2):
    """
    Apply a vignette filter to an image by darkening the borders while keeping the center bright.
    :param img: Input image
    :param level: Intensity of the vignette effect (default is 2)
    :return: Image with vignette effect applied
    """
    height, width = img.shape[:2]  # Extract the image dimensions (height, width)

    # Generate Gaussian kernels for both X and Y axes, which will be used to create the vignette mask
    X_resultant_kernel = cv2.getGaussianKernel(width, width/level)
    Y_resultant_kernel = cv2.getGaussianKernel(height, height/level)
        
    # Generating the final kernel matrix by multiplying the two Gaussian kernels
    kernel = Y_resultant_kernel * X_resultant_kernel.T 
    mask = kernel / kernel.max()  # Normalize the mask values to ensure they range from 0 to 1
    
    img_vignette = np.copy(img)  # Make a copy of the input image to apply the mask

    # Apply the mask to each of the three channels (R, G, B) of the image
    for i in range(3):
        img_vignette[:,:,i] = img_vignette[:,:,i] * mask  # Multiply the mask with each channel
    
    return img_vignette  # Return the image with vignette effect

# Choose an image to apply the vignette effect (in this case, 'flower' is chosen)
img = flower
img_vignette = vignette(img)  # Apply vignette filter to the image

# Display the original and filtered (vignette) image side by side for comparison
plot(img, img_vignette)

# Save the vignette image in the 'vignette' folder
vignette_image_path = os.path.join(vignette_folder, 'Flower_vignette.jpg')
cv2.imwrite(vignette_image_path, img_vignette)  # Save the vignette-filtered image
print(f"Vignette image saved at: {vignette_image_path}")

plt.show()  # Display the figure to the user
