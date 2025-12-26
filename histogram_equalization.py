import cv2
import matplotlib.pyplot as plt

# Read input image
img = cv2.imread("images/input.jpg")

if img is None:
    print("Error: Image not found")
    exit()

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply Histogram Equalization
equalized = cv2.equalizeHist(gray)

# Save output image
cv2.imwrite("output/histogram_equalization.jpg", equalized)

# Display image
plt.imshow(equalized, cmap="gray")
plt.title("Histogram Equalized Image")
plt.axis("off")
plt.show()
