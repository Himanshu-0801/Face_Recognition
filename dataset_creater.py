#importing packages 

import cv2 #opencv camera 
import  numpy as np # 
import sqlite3

faceDetect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') # to detect the face  
cam= cv2.VideoCapture(0) # to start the camera

def insertorupdate(ID,Name,age):
    conn= sqlite3.connect("FaceBase.db") # connecting to the database
    