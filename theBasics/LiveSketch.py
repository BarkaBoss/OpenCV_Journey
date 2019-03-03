import cv2

def sketch(image):
    imageGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    imageBlur = cv2.GaussianBlur(imageGray, (5,5), 0)
    imageEdge = cv2.Canny(imageBlur, 10,70)
    ret, mask = cv2.threshold(imageEdge, 70, 255, cv2.THRESH_BINARY_INV)
    return mask

cap = cv2.VideoCapture(0)
#fourcc = cv2.VideoWriter_fourcc(*'MP4V')
#out = cv2.VideoWriter('../vids/liveSketch.avi', -1, 20.0, (640, 480))
while True:
    ret, frame = cap.read()
    cv2.imshow("Live Sketch", sketch(frame))
    #outFrame = sketch(frame)
    #out.write(outFrame)
    if(cv2.waitKey(1) == 13):
        break
cap.release()
#out.release()
cv2.destroyAllWindows()