import cv2
img = cv2.imread("solar-system.jpg")
cv2.putText(img, "Sun", (8,220), cv2.FONT_HERSHEY_COMPLEX, 1.5, (255,255,255))
cv2.putText(img, "Mercury", (100,180), cv2.FONT_HERSHEY_COMPLEX, 0.7, (255,255,255))
cv2.putText(img, "Venus", (170,270), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255))
cv2.putText(img, "Earth", (260,150), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255))
cv2.putText(img, "Mars", (365,270), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255))
cv2.putText(img, "Jupiter", (500,80), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255))
cv2.putText(img, "Saturn", (730,340), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255))
cv2.putText(img, "Uranus", (925,130), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255))
cv2.putText(img, "Neptune", (1080,310), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255))
cv2.imshow("output", img)
cv2.waitKey(0)
cv2.imwrite("Solar_systemwithname.jpg", img)