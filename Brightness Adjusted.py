import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread("images/input.jpg")
if img is None:
    print("Error: Image not found")
    exit()

# Increase brightness
bright = cv2.convertScaleAbs(img, alpha=1, beta=50)

cv2.imwrite("output/brightness.jpg", bright)

bright_rgb = cv2.cvtColor(bright, cv2.COLOR_BGR2RGB)
plt.imshow(bright_rgb)
plt.title("Brightness Adjusted Image")
plt.axis("off")
plt.show()
