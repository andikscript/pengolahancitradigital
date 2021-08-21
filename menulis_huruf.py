import cv2 
from matplotlib import pyplot as plt

img = cv2.imread('sawah.jpg')

# font untuk menentukan tipe dari font yang dipakai
font = cv2.FONT_HERSHEY_SIMPLEX
# text untuk menentukan text yang akan ditampilkan
text = 'Petani Tembakau'
# org untuk menentukan letak teks berdasarkan garis
org = (500,250)
# fontScale untuk menentukan skala dari huruf yang tampil
fontScale = 1

color = (255,0,0)

thickness = 2

# cv2.putText untuk menempelkan text kedalam image
cv2.putText(img,text,org,font,fontScale,color,thickness,cv2.LINE_AA)

plt.imshow(img)

plt.show()
