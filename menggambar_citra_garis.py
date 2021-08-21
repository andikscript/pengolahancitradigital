import cv2 
from matplotlib import pyplot as plt

img = cv2.imread('sawah.jpg')

# (x,y)
# start_point dan end_point adalah variable yang digunakan 
# untuk patokan garis yang akan di buat
start_point = (150,0)
endpoint = (200, 100)
color = (255,0,0)
thickness = 5

# cv2.line.... digunakan untuk merender garis dan menempelkan
# pada image
cv2.line(img,start_point,endpoint,color,thickness)

plt.imshow(img)

plt.show()