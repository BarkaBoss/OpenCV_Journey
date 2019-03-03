import cv2

img = cv2.imread("../images/omene.jpg")

print(img.shape)

imgHeight = img.shape[0]
imgWidth = img.shape[1]
imgChannels = img.shape[2]

print("Height: ",imgHeight)
print("Width: ",imgWidth)
print("Channels: ",imgChannels)

cv2.imshow("Egg head", img)
cv2.waitKey()
cv2.destroyAllWindows()

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
print("Gray Image Shape: ",imgGray.shape)

imgSmall = cv2.resize(imgGray, (int(imgWidth/2), int(imgHeight/2)))
cv2.imshow("Gray Egg Head", imgSmall)
cv2.waitKey()
cv2.destroyAllWindows()