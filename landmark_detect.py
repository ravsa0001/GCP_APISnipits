# Importing the necessary libraries
import os
from google.cloud import vision

# Making A VISION API Client
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"/home/vo1d/Desktop/VS_Code/googleAPI/translate.json"
client = vision.ImageAnnotatorClient()

def detect_landmarks(path):
    # Reading the image
    with open(path, "rb") as image_file:
        content = image_file.read()
    image = vision.Image(content=content)

    # Detecting the landmark 
    response = client.landmark_detection(image=image)
    landmarks = response.landmark_annotations
    print("Landmarks:")

    # Print the name of the landmark with its longitude and latitude    
    for landmark in landmarks:
        print(landmark.description)
        for location in landmark.locations:
            lat_lng = location.lat_lng
            print(f"Latitude {lat_lng.latitude}")
            print(f"Longitude {lat_lng.longitude}")


detect_landmarks("/home/vo1d/Desktop/VS_Code/googleAPI/kedar.jpeg")