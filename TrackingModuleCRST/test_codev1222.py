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

filename = "savedIMG.jpg"
cv2.imwrite(filename, img)
last_bbox = bbox



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

        # memory_img = cv2.imread(filename,cv2.IMREAD_COLOR)
        # tracker.init(memory_img, last_bbox)


    

    fps = cv2.getTickFrequency()/(cv2.getTickCount()-timer)
    cv2.putText(img, str(int(fps)),(10,30),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,255,0),2)

    cv2.imshow("track", img)

    k =cv2.waitKey(1)
    if k == ord("q"):
        break

    if k == ord("i"): # Press "i" MANUAL REINIT BUTTON
        # bbox = cv2.selectROI("track",img,False)
        # print(bbox)

        memory_img = cv2.imread(filename,cv2.IMREAD_COLOR)
        tracker.init(memory_img, last_bbox)
        print("done init")

    if k == ord("k"):
        cv2.imwrite(filename, img)
        last_bbox = bbox
        print("done save")

    print("{cb} == {lb}" .format(cb=bbox,lb=last_bbox))

    