import cv2
import numpy as np
import matplotlib.pyplot as plt
import os
import json
import matplotlib  # Import matplotlib to set the backend

# Ensure Matplotlib uses an interactive backend for displaying images
matplotlib.use('TkAgg')

# Load configuration
with open('/Users/arinzemomife/Photoshop-Filters-Showcase/config.json') as config_file:
    config = json.load(config_file)

# Get image path from the config file
image_path = config.get('image_path')

if not image_path:
    raise ValueError("Image path not found in configuration file.")

# Define folders to save original and filtered images
original_folder = os.path.join('filtered', 'originals')
bw_folder = os.path.join('filtered', 'black_and_white')

# Ensure both the original and black_and_white folders exist
if not os.path.exists(original_folder):
    os.makedirs(original_folder)
if not os.path.exists(bw_folder):
    os.makedirs(bw_folder)

# Load images using the correct base path and file names
flower = cv2.imread(os.path.join(image_path, 'Flowers.jpg'))
house = cv2.imread(os.path.join(image_path, 'House.jpg'))
monument = cv2.imread(os.path.join(image_path, 'Monument.jpg'))
santorini = cv2.imread(os.path.join(image_path, 'Santorini.jpg'))
new_york = cv2.imread(os.path.join(image_path, 'New_York.jpg'))
coast = cv2.imread(os.path.join(image_path, 'California_Coast.jpg'))

# Check if the images are loaded successfully
if flower is None or house is None or monument is None or santorini is None or new_york is None or coast is None:
    print("Error: One or more sample images could not be loaded. Check the file paths.")
else:
    print("All images loaded successfully!")

# Define the plot function to display images
def plot(img1, img2):
    fig = plt.figure(figsize=(20, 10))
    
    # Display the original image
    plt.subplot(1, 2, 1)
    plt.imshow(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))  # Convert BGR to RGB for matplotlib
    plt.axis('off')
    plt.title("Original Image")
   
    # Display the filtered image
    plt.subplot(1, 2, 2)
    plt.imshow(cv2.cvtColor(img2, cv2.COLOR_BGR2RGB))  # Convert BGR to RGB for matplotlib
    plt.axis('off')
    plt.title("Filtered Image")

    plt.show()
    plt.close()  # Close the plot after displaying the images

# Define a function to save both the original and the filtered image
def save_images(img, img_name):
    # Save the original image
    original_path = os.path.join(original_folder, f'{img_name}_original.jpg')
    cv2.imwrite(original_path, img)
    print(f"Saved original: {original_path}")
    
    # Apply Black & White (grayscale) filter and save the filtered image
    img_bw = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    bw_path = os.path.join(bw_folder, f'{img_name}_bw.jpg')
    cv2.imwrite(bw_path, img_bw)
    print(f"Saved Black & White: {bw_path}")
    
    return img_bw  # Return the filtered image for comparison/display

# Save both the original and Black & White filtered images for each image
flower_bw = save_images(flower, 'flower')
house_bw = save_images(house, 'house')
monument_bw = save_images(monument, 'monument')
santorini_bw = save_images(santorini, 'santorini')
new_york_bw = save_images(new_york, 'new_york')
coast_bw = save_images(coast, 'california_coast')

# Example usage of the plot function to display original and Black & White images
plot(flower, flower_bw)  # Display original and Black & White version of flower
plot(house, house_bw)    # Display original and Black & White version of house
plot(monument, monument_bw)  # Display original and Black & White version of monument
