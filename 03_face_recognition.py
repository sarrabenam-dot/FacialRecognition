import picamera
import cv2
import numpy as np
import os
import sys
import datetime
import time

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer/trainer.yml')
cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath);

font = cv2.FONT_HERSHEY_SIMPLEX

#iniciate id counter
id = 0

# names related to ids
names = ['None', 'Yassine', 'Aida', 'Hichem', 'Hsan', 'Omar'] 

# Initialize and start realtime video capture
cam = cv2.VideoCapture(0)
cam.set(3, 480) # set video widht
cam.set(4, 320) # set video height

# Define min window size to be recognized as a face
minW = 0.1*cam.get(3)
minH = 0.1*cam.get(4)

while True:
    ret, img =cam.read()
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale( 
        gray,
        scaleFactor = 1.2,
        minNeighbors = 5,
        minSize = (int(minW), int(minH)),
       )

    for(x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)

        id, confidence = recognizer.predict(gray[y:y+h,x:x+w])

        # Check if confidence is less them 100 ==> "0" is perfect match 
        if (confidence < 100):
            idName = names[id]
            confidence = "  {0}%".format(round(confidence))
        else:
            idName = "unknown"
            confidence = "  {0}%".format(round(confidence))
        
        cv2.putText(img, str(idName), (x+5,y-5), font, 1, (255,255,255), 2)
        cv2.putText(img, str(confidence), (x+5,y+h-5), font, 1, (255,255,0), 1)

        
        if idName != 'None':
            print("\n you are " + idName + " with a precision of" + confidence)
            date = datetime.date.today().strftime("%d-%b-%Y")
            time = datetime.datetime.now().strftime("%H:%M:%S")
            print("\n date: " + date)
            print("\n time :" + time)            
            cv2.imwrite(str(id) + ".jpg", gray[y:y+h,x:x+w])
            sys.exit(0)
            
        elif idName == 'unknown':
            print("\n you are " + idName)
            break
         
    cv2.imshow('FacePointer',img) 

    k = cv2.waitKey(10) & 0xff # Press 'ESC' for exiting video
    if k == 27:
        break
    
# Do a bit of cleanup
print("\n [INFO] Exiting Program and cleanup stuff")
cam.release()
cv2.destroyAllWindows()
