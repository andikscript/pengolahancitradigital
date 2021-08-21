import cv2 
from matplotlib import pyplot as plt

img = cv2.imread('sawah.jpg')

# (x,y)
start_point = (600,5)
endpoint = (700, 100)
color = (255,0,0)
thickness = 2

cv2.rectangle(img,start_point,endpoint,color,thickness)

plt.imshow(img)

plt.show()