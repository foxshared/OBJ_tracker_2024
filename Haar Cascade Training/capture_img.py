import cv2

cap = cv2.VideoCapture(1)

count = 0
 
while True:
    success, img = cap.read()

    cv2.imshow("track", img)

    k =cv2.waitKey(1)
    if k == ord("q"):
        break
    
    

    if k == ord("p"):
        filename = ("Capture_img/{count}.jpg" .format(count=count))
        cv2.imwrite(filename, img)
        count += 1

        print(count)
