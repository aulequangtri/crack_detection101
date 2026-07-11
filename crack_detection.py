import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image (replace with your image path)
image_path = 'canva.jpg'
img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

#Step 1: Advanced Noise Reduction using Bilateral Filter
# Bilateral filter smooths the image while preserving edges
filtered_img = cv2.bilateralFilter(img, d=3, sigmaColor=75, sigmaSpace=75)

# Step 2: Edge Detection using Adaptive Canny Thresholds
# Compute median of the pixel intensities for adaptive thresholds
median_val = np.median(filtered_img)
lower_thresh = int(max(0, 0.6 * median_val))
upper_thresh = int(min(255, 1.33 * median_val))

# Apply Canny edge detection using the computed adaptive thresholds
edges = cv2.Canny(filtered_img, lower_thresh, upper_thresh) # Detects edges using the Canny edge detector

# Step 3: Morphological Operations for better edge continuity
kernel = np.ones((3, 3), np.uint8)

# First, use closing to close small gaps in the cracks
closed_edges = cv2.morphologyEx(edges, cv2.MORPH_CLOSE, kernel, iterations=2)

# Then, apply dilation to enhance the cracks further
dilated_edges = cv2.dilate(closed_edges, kernel, iterations=1)

# Step 4: Contour Detection from the dilated edges
contours, _ = cv2.findContours(dilated_edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Filter small contours based on area or length
min_contour_area = 100 # Minimum contour area threshold to remove noise
filtered_contours = [c for c in contours if cv2.contourArea(c) > min_contour_area]

# Step 5: Drawing Contours on the original image for better visualization
output_img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR) # Convert grayscale to BGR for colored drawing
cv2.drawContours(output_img, filtered_contours, -1, (0, 255, 0), 2) # Draw contours in green

# Visualization using Matplotlib
plt.figure(figsize=(10, 5))

# Original Image
plt.subplot(1, 3, 1)
plt.title('Original Image')
plt.imshow(img, cmap='gray')

# Final Output with Contours
plt.subplot(1, 3, 3)
plt.title('Crack Detected (Contours)')
plt.imshow(cv2.cvtColor(output_img, cv2.COLOR_BGR2RGB)) # Convert BGR to RGB for correct color display

plt.show()

# Optional: Save the output image with drawn contours
cv2.imwrite('precise_crack_contour_output.jpg', output_img)
