import cv2
import numpy as np

face_classifier = cv2.CascadeClassifier("haar/haarcascade_frontalface_default.xml")
image =  cv2.imread("images/omene.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

faces = face_classifier.detectMultiScale(gray, 1.3, 5)

if faces is():
    print("No face found")

for (x,y,w,h) in faces:
    cv2.rectangle(image,(x,y), (x+w, y+h), (127,0,255), 2)
    cv2.imshow('Face Detect', image)
    cv2.waitKey(0)
cv2.destroyAllWindows()