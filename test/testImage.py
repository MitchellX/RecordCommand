import matplotlib.pyplot as plt
from PIL import Image
import cv2

image = Image.open('C:/Users/xmc/Pictures/umass/umass1.jpg')
print(image.size)

print(image.mode)
plt.imshow(image)
plt.show()