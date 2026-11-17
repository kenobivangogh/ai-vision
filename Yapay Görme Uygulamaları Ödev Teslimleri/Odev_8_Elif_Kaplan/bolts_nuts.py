import cv2
import numpy as np

def template_matching(image_path, template_path, threshold=0.5,  overlap_thresh=0.3):
    # Ana görüntü
    image = cv2.imread(image_path)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Şablon görüntü
    template = cv2.imread(template_path, cv2.IMREAD_GRAYSCALE)
    template_height, template_width = template.shape[:2]

    # Template Matching uygulamak
    result = cv2.matchTemplate(gray_image, template, cv2.TM_CCOEFF_NORMED)
    locations = np.where(result >= threshold)

    rectangles = []
    for (x, y) in zip(*locations[::-1]):
        rectangles.append([int(x), int(y), int(template_width), int(template_height)])
        rectangles.append([int(x), int(y), int(template_width), int(template_height)])
    
    # Non-Maximum Suppression (NMS) ile üst üste binen eşleşmeleri filtrelemek
    rectangles, weights = cv2.groupRectangles(rectangles, groupThreshold=1, eps=overlap_thresh)

    return rectangles

def draw_matches(image, matches, template_width, template_height):
    for (x, y, w, h) in matches:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
    return image   

# Ana resim ve şablon resimlerinin dosya yolları
image_path = "bolts_nuts.jpg"
bolt_template_path = "bolt_template.jpg"
nut_template_path = "nut_template.jpg"

# Cıvata ve somun şablonlarını eşleştir
bolt_matches = template_matching(image_path, bolt_template_path, threshold=0.5, overlap_thresh=0.5)
nut_matches = template_matching(image_path, nut_template_path, threshold=0.5, overlap_thresh=0.5)

# Sonuçlar
print(f"Cıvata sayısı: {len(bolt_matches)}")
print(f"Somun sayısı: {len(nut_matches)}")

image = cv2.imread(image_path)
bolt_template = cv2.imread(bolt_template_path, cv2.IMREAD_GRAYSCALE)
nut_template = cv2.imread(nut_template_path, cv2.IMREAD_GRAYSCALE)

# Eşleşmeleri çiz
image_with_bolts = draw_matches(image, bolt_matches, bolt_template.shape[1], bolt_template.shape[0])
image_with_nuts = draw_matches(image_with_bolts, nut_matches, nut_template.shape[1], nut_template.shape[0])

cv2.imshow("Detected Bolts and Nuts", image_with_nuts)
cv2.waitKey(0)
cv2.destroyAllWindows()
