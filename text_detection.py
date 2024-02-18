# Importing necessary libraries
import os, cv2
from google.cloud import vision

# Making A VISION API Client for Optical Character Recognition(OCR)
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"/home/vo1d/Desktop/VS_Code/googleAPI/translate.json"
client = vision.ImageAnnotatorClient()

# making a function for OCR
def detect_text(path):
    # Reading the input Image
    img = cv2.imread(path)

    with open(path, "rb") as image_file:
        content = image_file.read()
    image = vision.Image(content = content)

    # Detecting text in Image 
    response = client.text_detection(image = image)
    texts = response.text_annotations
    
    # Ploting the detections on the image
    for i in range(1, len(texts)):
        p1 = texts[i].bounding_poly.vertices[0]
        p2 = texts[i].bounding_poly.vertices[2]
        cv2.rectangle(img, (p1.x, p1.y), (p2.x, p2.y), (255, 0, 255), 2)
        
    cv2.imshow("image", img)
    cv2.waitKey(0)

# Calling the function to detect text in image
detect_text("/home/vo1d/Desktop/VS_Code/googleAPI/kuchtext.jpg")
detect_text("/home/vo1d/Desktop/VS_Code/googleAPI/text.png")
