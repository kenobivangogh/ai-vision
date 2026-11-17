import cv2
import numpy as np

image = cv2.imread('resim.jpg')

# Görüntünün boyutlarını almak
height, width, _ = image.shape

# Her bir sütunun genişliğini hesaplamak
column_width = width // 3

# Mavi (B) kanalı
blue_channel = image[:, :, 0]

# Yeşil (G) kanalı
green_channel = image[:, :, 1]

# Kırmızı (R) kanalı
red_channel = image[:, :, 2]

blue_image = cv2.merge([blue_channel, np.zeros((height, width), dtype=np.uint8), np.zeros((height, width), dtype=np.uint8)])
green_image = cv2.merge([np.zeros((height, width), dtype=np.uint8), green_channel, np.zeros((height, width), dtype=np.uint8)])
red_image = cv2.merge([np.zeros((height, width), dtype=np.uint8), np.zeros((height, width), dtype=np.uint8), red_channel])


# Görüntüleri ekranda göstermek
cv2.imshow('Blue Channel', blue_image[:, :column_width])
cv2.imshow('Green Channel', green_image[:, column_width:2*column_width])
cv2.imshow('Red Channel', red_image[:, 2*column_width:])

# Üç parçayı yan yana birleştirmek
combined_image = cv2.hconcat([blue_image[:, :column_width], green_image[:, column_width:2*column_width], red_image[:, 2*column_width:]])

# Birleştirilmiş görüntü
cv2.imshow('Combined Image', combined_image)
cv2.waitKey(0)
cv2.destroyAllWindows()