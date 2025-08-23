import os 
import cv2 
import numpy as np
from PIL import Image # for opening and the reading of images


recognizer = cv2.face.LBPHFaceRecognizer_create() # to recognize faces
path = "dataset"

def get_images_and_labels(path):
    images_paths = [os.path.join(path, f) for f in os.listdir(path)] # get the image paths
    faces =[]
    ids = []
    for single_image_path in images_paths:
        faceImg = Image.open(single_image_path).convert("L") # convert to grayscale
        faceNp = np.array(faceImg, "uint8") # convert to numpy array
        id = int(os.path.split(single_image_path)[-1].split(".")[1]) # get the ID from the image name
        print(id)
        faces.append(faceNp) # append the face to the list
        ids.append(id) # append the ID to the list
        cv2.imshow("training", faceNp) # show the image being trained
        cv2.waitKey(10) # wait for 10ms
    return np.array(ids), faces

ids, faces = get_images_and_labels(path)
recognizer.train(faces, ids) # train the recognizer
recognizer.save("recognizer/trainingData.yml")
cv2.destroyAllWindows() # close all windows
