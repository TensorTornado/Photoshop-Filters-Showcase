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

# Define the folder to save Black & White images
output_folder = os.path.join('filtered', 'black_and_white')

# Ensure the output folder exists
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

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

# Define a function to apply Black & White filter and save the result
def save_bw_filter(img, img_name):
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # Convert to Black & White (grayscale)
    output_path = os.path.join(output_folder, f'{img_name}_bw.jpg')  # Define save path
    cv2.imwrite(output_path, img_gray)  # Save the image
    print(f"Saved: {output_path}")  # Confirmation message

# Apply Black & White filter to each image and save it
save_bw_filter(flower, 'flower')
save_bw_filter(house, 'house')
save_bw_filter(monument, 'monument')
save_bw_filter(santorini, 'santorini')
save_bw_filter(new_york, 'new_york')
save_bw_filter(coast, 'california_coast')

# Example usage of the plot function to display original and Black & White images
plot(flower, cv2.imread(os.path.join(output_folder, 'flower_bw.jpg')))  # Display original and BW version
plot(house, cv2.imread(os.path.join(output_folder, 'house_bw.jpg')))     # Display house
plot(monument, cv2.imread(os.path.join(output_folder, 'monument_bw.jpg')))  # Display monument
plot(santorini, cv2.imread(os.path.join(output_folder, 'santorini_bw.jpg')))  # Display santorini
plot(new_york, cv2.imread(os.path.join(output_folder, 'new_york_bw.jpg')))  # Display New York
plot(coast, cv2.imread(os.path.join(output_folder, 'california_coast_bw.jpg')))  # Display California Coast