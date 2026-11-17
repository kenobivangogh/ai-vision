import cv2
import numpy as np

# Gürültülü görüntü
noisy_image = cv2.imread('noisy_image.png', cv2.IMREAD_GRAYSCALE)

# Gauss filtresi
denoised_image = cv2.GaussianBlur(noisy_image, (5, 5), 0)

# Threshold yöntemini kullanarak temizlenmiş görüntü elde etmek
_, thresholded_image = cv2.threshold(denoised_image, 127, 255, cv2.THRESH_BINARY)

# Gürültülü ve Temizlenmiş görüntüleri göster
cv2.imshow('Noisy Image', noisy_image)
cv2.imshow('Denoised Image', denoised_image)
cv2.imshow('Cleaned Image', thresholded_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
