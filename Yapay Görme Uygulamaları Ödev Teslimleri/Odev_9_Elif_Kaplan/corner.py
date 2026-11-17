import cv2
import numpy as np

def shi_tomasi_corner_detection(image_path):
    
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Shi-Tomasi köşe tespiti
    corners = cv2.goodFeaturesToTrack(gray, maxCorners=100, qualityLevel=0.01, minDistance=10)
    corners = np.int0(corners)
    
    # Köşeleri görüntüde işaretle
    for i in corners:
        x, y = i.ravel()
        cv2.circle(image, (x, y), 3, 255, -1)
    

    cv2.imshow('Shi-Tomasi Corners', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

shi_tomasi_corner_detection("part.jpg")
