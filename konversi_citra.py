# import digunakan untuk meminta library untuk
# menampilkan gambar
import cv2 
from matplotlib import pyplot as plt

# img disini adalah variable yang menyimpan dari gambar 
# yang akan ditampilkan
img = cv2.imread('sawah.jpg')

# imgKonversi adalah mengkonversi gambar yang disimpan 
# dalam variable ke warna yang dikehendaki
# imgKonversi = cv2.cvtColor(img, cv2.COLOR_RGB2HLS)

# plt.imshow() digunakan menyimpan gambar 
# yang akan ditampilkan ke layar
plt.imshow(imgKonversi)

# plt.show() digunakan untuk menampilkan gambar ke layar
plt.show()