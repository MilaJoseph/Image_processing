import cv2
import matplotlib.pyplot as plt

img = cv2.imread("images/input.jpg")
if img is None:
    print("Error: Image not found")
    exit()

# Increase contrast
contrast = cv2.convertScaleAbs(img, alpha=1.5, beta=0)

cv2.imwrite("output/contrast.jpg", contrast)

contrast_rgb = cv2.cvtColor(contrast, cv2.COLOR_BGR2RGB)
plt.imshow(contrast_rgb)
plt.title("Contrast Enhanced Image")
plt.axis("off")
plt.show()
