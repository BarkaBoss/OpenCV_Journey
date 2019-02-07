import cv2

face_classifier = cv2.CascadeClassifier('haar/haarcascade_frontalface_default.xml')
eye_classifier = cv2.CascadeClassifier('haar/haarcascade_eye.xml')
image = cv2.imread("images/lv.jpg")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

faces = face_classifier.detectMultiScale(gray, 1.3, 5)

if faces is ():
    print("No face found")

for(x,y,w,h) in faces:
    cv2.rectangle(image, (x,y), (x+w, y+h), (127,25,155), 2)
    #cv2.imshow("Face n Eye", image)
    #cv2.waitKey(0)

    #finding eyes within region of interest
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = image[y:y+h, x:x+w]

    eyes = eye_classifier.detectMultiScale(roi_gray)

    for(ex,ey,ew,eh) in eyes:
        cv2.rectangle(roi_color,(ex, ey), (ex+ew, ey+eh), (255, 255, 0), 2)
        print("x "+ str(ex) +" y "+ str(ey) +" w "+str(ew)+" h "+str(eh))
        cX, cY = int(ex+ew/2), int(ey+eh/2)
        #print("WidthC " + str(cX) + " HeightC " + str(cY))
        cv2.circle(roi_color,(cX, cY), eh, (125,75,62), 4)
        cv2.imshow('Eyes', image)
        cv2.waitKey(0)
        cv2.imwrite("face_n_eye.jpg", image)

cv2.destroyAllWindows()