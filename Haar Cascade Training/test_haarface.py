import cv2

eye_cascade = cv2.CascadeClassifier("haarcascade_eye.xml")

img = cv2.imread("face.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

eye = eye_cascade.detectMultiScale(gray,1.1,4)

for (x,y,w,h) in eye:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

cv2.imshow("img",img)

cv2.waitKey()