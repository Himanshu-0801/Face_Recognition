import cv2
import numpy as np
import os
import sqlite3


facedetect = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
cam = cv2.VideoCapture(0) # the zero is to use the default camera 

recognizer = cv2.face.LBPHFaceRecognizer_create() # create the recognizer
recognizer.read("recognizer/trainingData.yml") # read the trained data

def getProfile(id):
    conn = sqlite3.connect("FaceBase.db") # connect to the database
    cursor = conn.execute("SELECT * FROM STUDENT WHERE ID=?", (id,)) # execute the query
    profile = None
    for row in cursor:
        profile = row
    conn.close()
    return profile

while True:
    ret,img =cam.read() # read the image from the camera
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # convert the image to grayscale   
    faces = facedetect.detectMultiScale(gray, 1.3, 5) # detect the faces in the image
    for (x,y,w,h) in faces: 
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        id, conf = recognizer.predict(gray[y:y+h,x:x+w])
        profile = getProfile(id)
        if(profile != None):
            cv2.putText(img, "Name: " + str(profile[1]), (x, y+h+30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)
            cv2.putText(img, "Age: " + str(profile[2]), (x, y+h+60 ), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)
            
    cv2.imshow("Face",img)
    if cv2.waitKey(1)==ord('q'): # wait for the user to quit
        break
cam.release() # release the camera
cv2.destroyAllWindows() # close all windows
 