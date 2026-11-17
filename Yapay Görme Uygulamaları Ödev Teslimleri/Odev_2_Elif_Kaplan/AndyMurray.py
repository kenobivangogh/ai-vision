import cv2
import numpy as np

img = cv2.imread('AndyMurray.jpg')

# resmin boyutu
row , column , _ = img.shape

print("row:", row)
print("column:", column)

#resmin kopyalanacak parçası #1
x1, y1 = 613, 683
x2, y2 = 712, 768

cropped_Area = img[y1:y2 , x1:x2]

#resmin kopyalanacak parçası #2

x1_1, y1_1 = 468, 683
x2_1, y2_1 = 567, 768

cropped_Area1 = img[y1_1:y2_1 , x1_1:x2_1]

cv2.imshow("Image", cropped_Area)
cv2.imshow("Image2", cropped_Area1)

#parçaları kopyalama

img[300:385 , 972:1071] = cropped_Area
img[y1:y2 , x1:x2] = cropped_Area1

# Yazı rengi ve boyutu
yazi_rengi = (255, 255, 255)  # Beyaz renk
yazi_boyutu = 0.7
font = cv2.FONT_HERSHEY_SIMPLEX

# Metni resmin sol üst köşesine ekleme
metin = "Elif Kaplan"
cv2.putText(img, metin, (0, 50), font, yazi_boyutu, yazi_rengi, 2)

#manipüle resmi başka isimle kaydetme

cv2.imwrite("manip_picture.jpg", img)

#manipüle edilmiş resim

cv2.imshow("Image3", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

