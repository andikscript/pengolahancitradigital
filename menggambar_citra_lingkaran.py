import cv2 
from matplotlib import pyplot as plt

img = cv2.imread('sawah.jpg')

# (center,center) dari lingkaran
center = (650,100)
radius = 100
color = (255,0,0)
thickness = 2

cv2.circle(img,center,radius,color,thickness)

plt.imshow(img)

plt.show()