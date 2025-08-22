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