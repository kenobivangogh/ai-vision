import cv2

image = cv2.imread('image.png', cv2.IMREAD_GRAYSCALE)

# Histogram eşitleme işlemi
equ = cv2.equalizeHist(image)

cv2.imwrite('improved_image.png', equ)

cv2.imshow("Original image", image)
cv2.imshow("Improved image", equ)
cv2.waitKey(0)
cv2.destroyAllWindows()

