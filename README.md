# Photoshop-Filters-Showcase
A Photoshop Filters Portfolio
*****************************
## Project Overview
This project demonstrates the application of various artistic filters to images using Python and OpenCV. The goal is to showcase technical expertise in image manipulation and automation using Python, as well as to highlight creative problem-solving using image processing techniques.

Each filter is designed to alter the image in a unique way, demonstrating different aspects of image processing such as edge detection, color transformation, and exposure adjustment. This portfolio not only reflects strong programming capabilities but also an eye for aesthetics and detail.
 project demonstrating various Photoshop filters like Black &amp; White, Sepia, Canny Edge Detection, and more.

********************************
## Filters Applied
Below are the filters applied to the images, along with a brief description of each:

1. **Black and White Filter**: Converts an image to grayscale, highlighting contrast and texture.
2. **Sepia/Vintage Filter**: Adds a warm, aged look to an image, similar to vintage photos.
3. **Vignette Effect**: Darkens the corners of an image, drawing focus to the center.
4. **Edge Detection (Canny)**: Detects the edges of objects within an image, highlighting them in a stylized form.
5. **Exposure Improvement**: Enhances brightness and contrast, making the image more vivid.
6. **Outline Filter**: Extracts and highlights the outlines of objects in the image.
7. **Pencil Sketch Filter**: Converts an image into a hand-drawn pencil sketch style.
8. **Stylization Filter**: Applies an artistic, smooth effect to give the image a painterly feel.

*************************************************************************************************

# Reuirements and setup:
Python 3.11
OpenCV 4.9
Numpy
Matplotlib (for visualizations)

## Folder Structure

```bash
Photoshop-Filters-Portfolio/
│
├── images/
│   ├── filtered/                     # Filtered images
│   │   ├── black_and_white/          # Filtered images using Black & White filter
│   │   ├── edge_detection/           # Filtered images using Edge Detection filter
│   │   ├── exposure_improvement/     # Filtered images using Exposure Improvement filter
│   │   ├── outline/                  # Filtered images using Outline filter
│   │   ├── sepia/                    # Filtered images using Sepia filter
│   │   ├── stylization/              # Filtered images using Stylization filter
│   │   ├── vignette/                 # Filtered images using Vignette filter
│   ├── original/                     # Directory containing original images
│   │   └── (various original images) 
│
├── results/                          # Directory for any additional results
│
├── scripts/                          # Python scripts for each filter
│   ├── black_and_white.py            # Script for applying Black & White filter
│   ├── edge_detection.py             # Script for Canny Edge Detection
│   ├── exposure_improvement.py       # Script for Exposure Improvement
│   ├── outline.py                    # Script for applying Outline filter
│   ├── pencil_sketch.py              # Script for Pencil Sketch filter
│   ├── sepia.py                      # Script for applying Sepia filter
│   ├── stylization.py                # Script for Stylization filter
│   ├── vignette.py                   # Script for Vignette filter
│
└── README.md                         # Project description and instructions (this file)

****************************************************************************************

### Technologies Used
- **Python**: The primary programming language used for image manipulation and automation.
- **OpenCV**: A popular computer vision library used for image processing.
- **NumPy**: Used for numerical operations, especially for matrix manipulations and pixel adjustments.
- **Matplotlib**: A library used for visualizing the output before and after applying filters.


###Results
##Before-and-After Images

| Filter            | Original Image                           | Filtered Image                            |
|-------------------|------------------------------------------|-------------------------------------------|
| Bl_w              | ![original](images/original_image.jpg)   | ![bl_w](images/filtered/bl_w              |
| Sepia             | ![original](images/original_image.jpg)   | ![sepia](images/filtered/sepia.jpg)       |
| Vignette          | ![original](images/original_image.jpg)   | ![vignette](images/filtered/vignette.jpg) |
| Edge Detection    | ![original](images/original_image.jpg)   | ![edge_detection](images/filtered/edge_detection.jpg)

*********************************************************************************************************************
Observations:

Filter Application on Different Image Types
Filters like Sepia and Vignette performed well on images with low contrast, whereas Edge Detection and Sketch excelled in images with high contrast.

Image Size and Performance
Large image files required careful memory management, especially when applying computationally heavy filters like Stylization.

Automation Benefits
Batch processing via Python scripts reduced the time spent on applying filters manually in Photoshop, allowing for quick testing of different filter combinations.

*********************************************************************************************************************
## Challenges Faced and Solutions

### 1. Image Color Manipulation and Conversion
**Challenge**: One of the biggest challenges was ensuring the correct color conversion between BGR (OpenCV's default color format) and RGB (used by most display libraries such as Matplotlib). Images processed in BGR would appear distorted when displayed using Matplotlib.

**Solution**: The solution was to consistently convert images from BGR to RGB before displaying them. I used `cv2.cvtColor(img, cv2.COLOR_BGR2RGB)` for this transformation to ensure the colors were displayed correctly.

---

### 2. Handling Large Image Files
**Challenge**: Some images were too large, which caused performance issues during the application of filters, especially when trying to display or save the images after processing.

**Solution**: I resized the images to a manageable size using OpenCV’s `cv2.resize()` function before applying the filters. This not only improved performance but also kept the image quality intact for demonstration purposes.

---

### 3. Edge Detection Tuning
**Challenge**: The Canny Edge Detection filter was sensitive to the parameters provided, often resulting in too many or too few edges being detected.

**Solution**: I experimented with the `threshold1` and `threshold2` parameters of the `cv2.Canny()` function, adjusting the values based on the image’s contrast and brightness levels. Additionally, pre-processing steps such as blurring the image using `cv2.GaussianBlur()` helped to reduce noise and provide better results.

---

### 4. Implementing a Vignette Effect
**Challenge**: Adding a smooth vignette effect that darkens the corners without causing harsh transitions was initially difficult, as OpenCV does not provide a built-in function for this effect.

**Solution**: I created a mask using a Gaussian kernel to smoothly apply the vignette effect. By multiplying the original image with this mask, I was able to achieve the desired darkening effect around the image corners, with a smooth transition to the center.

---

### 5. Maintaining Image Quality After Multiple Filter Applications
**Challenge**: Applying multiple filters on the same image caused degradation of image quality, especially after multiple rounds of processing, due to pixel rounding errors.

**Solution**: I ensured that each filter was applied independently on the original image rather than stacking them on top of each other. This preserved the image quality while still showcasing the different effects.

*********************************************************************************************************************
## Conclusion

This portfolio project demonstrates a variety of filters and effects, providing a robust showcase of both creative image processing skills and technical expertise in Python programming. Each filter reflects mastery of computer vision techniques, making this an essential part of any brag portfolio in the domain of image processing.


