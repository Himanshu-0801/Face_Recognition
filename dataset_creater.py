#importing packages 

import cv2 #opencv camera 
import  numpy as np # 
import sqlite3

faceDetect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') # to detect the face  
cam= cv2.VideoCapture(0) # to start the camera

def insertorupdate(ID,Name,age):
    conn= sqlite3.connect("FaceBase.db") # connecting to the database
    cmd  = "SELECT * FROM STUDENT WHERE ID="+str(ID)
    cursor = conn.execute(cmd)
    isRecordExist = 0  # to check if record exists
    for row in cursor:
        isRecordExist = 1
    if isRecordExist == 1:
        cmd = ("UPDATE STUDENT SET Name=? WHERE ID=?", (Name, ID))
        cmd = ("UPDATE STUDENT SET  Age=? WHERE ID=?", (age, ID))
    else: # if record does not exists
        conn.execute("INSERT INTO STUDENT(ID,Name,Age) VALUES(?,?,?)", (ID, Name, age))
    conn.commit()
    conn.close() 
    
# insert the user defined values in the table 
ID  = input('Enter ID: ')
Name = input('Enter Name: ')
age = input('Enter Age: ')  

insertorupdate(ID, Name, age)

#detect face in web camrea coding 
sampleNum = 0 
while(True):
    ret,img = cam.read() # open the camera
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # convert to gray scale used to increase the accuracy
    faces = faceDetect.detectMultiScale(gray, 1.3, 5) # detect faces, 5 is the minNeighbors and 1.3 is the scaleFactor
    for (x,y,w,h) in faces:
        sampleNum = sampleNum + 1
        cv2.imwrite("dataset/User." + str(ID) + '.' + str(sampleNum) + ".jpg", gray[y:y+h, x:x+w])
        cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2)  # draw rectangle around the face to show face is being detected
        cv2.waitKey(100)    # wait for 100ms
    cv2.imshow("Face", img)  # show the image with rectangle
    cv2.waitKey(1)  # wait for 1ms
    if sampleNum > 20:  # take 20 samples and then stop
        break  #if sampleNum > 20:  # if 20 samples are taken, stop
    
cv2.release()  # release the camera    
cv2.destroyAllWindows()  # close all windows    

