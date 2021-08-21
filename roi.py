import cv2 
from matplotlib import pyplot as plt

img = cv2.imread('sawah.jpg')

# roi digunakan untuk memotong objek berdasarkan
# koordinat x,y 
roi = img[10:240,570:750]

plt.imshow(roi)

plt.show()