# Test custom Haar cascade
import cv2

custom_cascade = cv2.CascadeClassifier("cascadev3.xml")

cap = cv2.VideoCapture(1)

img1 = cv2.imread("face.jpg")

while True:
    ret, img = cap.read()

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.equalizeHist(gray)

    # print(custom_cascade.empty())
    # if custom_cascade is True:
    custom = custom_cascade.detectMultiScale(gray,4.3,10)

    for (x,y,w,h) in custom:
        cv2.rectangle(img,(x,y), (x+w,y+h),(255,0,0),2)


    cv2.imshow("Cascade Test",img)

    k = cv2.waitKey(1)
    if k == ord("q"):
        break