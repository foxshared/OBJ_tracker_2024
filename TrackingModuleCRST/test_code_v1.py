import cv2

cap = cv2.VideoCapture(1)

# tracker = cv2.legacy.TrackerMOSSE_create()
tracker = cv2.TrackerCSRT_create()

for x in range(0,5):
    success, img = cap.read()
    print("OK {}" .format(x))
    success = success
    img = img

bbox = cv2.selectROI("track",img,False)
tracker.init(img, bbox)

def drawbox():
    x,y,w,h = int(bbox[0]),int(bbox[1]),int(bbox[2]),int(bbox[3])
    cv2.rectangle(img,(x,y),((x+w),(y+h)),(255,0,10),3,1)
 
while True:
    timer = cv2.getTickCount()
    success, img = cap.read()
    success, bbox = tracker.update(img)
    if success:
        drawbox()
        cv2.putText(img, "Track",(10,70),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,255,0),2)
    else:
        print("OK {}" .format(success))
        cv2.putText(img, "Loss",(10,70),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,255,0),2)


    

    fps = cv2.getTickFrequency()/(cv2.getTickCount()-timer)
    cv2.putText(img, str(int(fps)),(10,30),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,255,0),2)

    cv2.imshow("track", img)

    k =cv2.waitKey(1)
    if k == ord("q"):
        break

    if k == ord("i"): # Press "i" MANUAL REINIT BUTTON
        bbox = cv2.selectROI("track",img,False)
        print(bbox)
        tracker.init(img, bbox)

    