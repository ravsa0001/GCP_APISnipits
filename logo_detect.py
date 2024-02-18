# Importing the necessary libraries
import os, cv2
from google.cloud import vision

# Making A VISION API Client
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"/home/vo1d/Desktop/VS_Code/googleAPI/translate.json"
client = vision.ImageAnnotatorClient()

def detect_logos(path):
    # Reaking the input Image
    img = cv2.imread(path)
    img = cv2.pyrDown(img)
    
    with open(path, "rb") as image_file:
        content = image_file.read()
    image = vision.Image(content=content)

    # Detecting the logo
    response = client.logo_detection(image=image)
    logos = response.logo_annotations
    print("Logos:")

    # Ploting the detection on the image
    for logo in logos:
        print(logo.description)
        org = logo.bounding_poly.vertices[0]
        cv2.putText(img, logo.description, (org.x, org.y-50), cv2.FONT_HERSHEY_SIMPLEX,
             1, (255, 0, 255), 2)
    cv2.imshow("Logo", img)
    cv2.waitKey(0)

# detect_logos("/home/vo1d/Desktop/VS_Code/googleAPI/images.jpeg")
detect_logos("/home/vo1d/Desktop/VS_Code/googleAPI/Adidas.png")
