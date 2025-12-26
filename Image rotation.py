import cv2
import matplotlib.pyplot as plt

img = cv2.imread("images/input.jpg")
(h, w) = img.shape[:2]

center = (w//2, h//2)
matrix = cv2.getRotationMatrix2D(center, 45, 1.0)

rotated = cv2.warpAffine(img, matrix, (w, h))

cv2.imwrite("output/rotation.jpg", rotated)

rot_rgb = cv2.cvtColor(rotated, cv2.COLOR_BGR2RGB)
plt.imshow(rot_rgb)
plt.title("Rotated Image")
plt.axis("off")
plt.show()
