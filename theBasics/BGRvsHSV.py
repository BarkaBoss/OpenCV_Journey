import cv2
import numpy as np

photo = cv2.imread("../images/lv.jpg")

B,G,R = cv2.split(photo)

zeros = np.zeros(photo.shape[:2], dtype="uint8")
cv2.imshow("Blue", cv2.merge([B, zeros, zeros]))
cv2.imshow("Green", cv2.merge([zeros, G, zeros]))
cv2.imshow("Red", cv2.merge([zeros, zeros, R]))

cv2.waitKey()
cv2.destroyAllWindows()