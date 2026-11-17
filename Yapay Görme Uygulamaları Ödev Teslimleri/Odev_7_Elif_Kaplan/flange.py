import cv2
import numpy as np

def check_flange_holes(image_path, min_radius=18, max_radius=20):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Gauss
    blurred = cv2.GaussianBlur(gray, (9, 9), 2)
    
    # Hough Circle Transform ile delikleri tespit etmek
    circles = cv2.HoughCircles(
        blurred, 
        cv2.HOUGH_GRADIENT, 
        dp=1.2, 
        minDist=20, 
        param1=50, 
        param2=30, 
        minRadius=min_radius, 
        maxRadius=max_radius
    )
    
    # delikleri çizmek ve saymak
    if circles is not None:
        circles = np.round(circles[0, :]).astype("int")
        valid_circle_count = 0

        for (x, y, r) in circles:
            if min_radius <= r <= max_radius:
                valid_circle_count += 1
                cv2.circle(image, (x, y), r, (0, 255, 0), 4)
            else:
                cv2.circle(image, (x, y), r, (0, 0, 255), 4)
        
        # Kontrol
        if valid_circle_count == 8:
            result = "PASS"
        else:
            result = "FAIL"
    else:
        result = "FAIL"

    # Sonucu yazdır
    print(result)

    cv2.imshow("Detected Circles", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Flanş görüntüsünün dosya yolu
image_path = "flange_fail2.png"

check_flange_holes(image_path)
