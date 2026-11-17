import cv2
import numpy as np

def perspective_correction(image_path):
  
    img = cv2.imread(image_path)
    height, width, _ = img.shape
    
    # Kitabın dört köşe noktasının koordinatları
    src_points = np.float32([[325, 25], [684, 17], [30, 590], [900, 570]]) # Örnek koordinatlar, kitabın köşelerine göre ayarlanmalı, ancak dosyanın izinlerini ayarlamama rağmen hata almaktayım, düzeltemedim.

    # Hedef konum
    dst_points = np.float32([[0, 0], [width, 0], [0, height], [width, height]])

    # Perspektif dönüşüm matrisi
    perspective_matrix = cv2.getPerspectiveTransform(src_points, dst_points)

    # Perspektif dönüşümünü
    corrected_img = cv2.warpPerspective(img, perspective_matrix, (width, height))

    cv2.imwrite("corrected_image.jpg", corrected_img)

    cv2.imshow("Corrected Image", corrected_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

perspective_correction("resim.jpg")
