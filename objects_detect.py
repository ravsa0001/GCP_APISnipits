# Importing the necessary libraries
import os, cv2
from google.cloud import vision

# Making A VISION API Client
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"/home/vo1d/Desktop/VS_Code/googleAPI/translate.json"
client = vision.ImageAnnotatorClient()

# Making the function to 
def localize_objects(path):
    img = cv2.imread(path)
    
    with open(path, "rb") as image_file:
        content = image_file.read()
    image = vision.Image(content = content)

    respeonse = client.object_localization(image = image)
    objects = respeonse.localized_object_annotations
    # print(objects)

    print(f"Number of objects found: {len(objects)}")
    
    # Ploting the detections on the image
    for object in objects:
        p1 = object.bounding_poly.normalized_vertices[0]
        p2 = object.bounding_poly.normalized_vertices[2]
        # print(p1.x, p2.x)
        width, height = img.shape[1], img.shape[0]
        cv2.putText(img, object.name, (int(p1.x*width), int(p1.y*height)-10), 
                    cv2.FONT_HERSHEY_SIMPLEX,1, (255, 0, 255), 2)
        
        cv2.rectangle(img, (int(p1.x*width), int(p1.y*height)), (int(p2.x*width), int(p2.y*height)), (255, 0, 255), 3)
        
    cv2.imshow("image", img)
    cv2.waitKey(0)

# localize_objects("/home/vo1d/Desktop/VS_Code/googleAPI/street.jpg")
localize_objects("/home/vo1d/Desktop/VS_Code/googleAPI/1257.jpg")
# localize_objects("/home/vo1d/Desktop/VS_Code/googleAPI/streets.jpeg")