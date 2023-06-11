import cv2
image = cv2.imread("Pic.jpeg")
grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
inverted = cv2.bitwise_not(grey)
blur = cv2.GaussianBlur(inverted,(45,45), 0)
invertedblur = cv2.bitwise_not(blur)

final = cv2.divide(grey, invertedblur, scale=246.0)
cv2.imshow("original image", image)
cv2.imshow("sketch image", final)
cv2.waitKey(0)