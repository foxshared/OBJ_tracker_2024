# Improve code structure using class

import cv2

class processing():
    def __init__(self):

        self.camera_cap = cv2.VideoCapture(1)
        self.tracker = cv2.TrackerKCF_create()
        for x in range(0, 5):
            success, self.img = self.camera_cap.read()
            print("OK {}" .format(x))
            success = success
            self.img = self.img

        self.bbox = cv2.selectROI("track", self.img, False)
        self.tracker.init(self.img, self.bbox)

        self.camera_process()

    def camera_process(self):
        timer = cv2.getTickCount()
        success, self.img = self.camera_cap.read()

        success, self.bbox = self.tracker.update(self.img)
        if success:
            self.drawbox()
            cv2.putText(self.img, "Track", (10, 70),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
        else:
            print("OK {}" .format(success))
            cv2.putText(self.img, "Loss", (10, 70),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
            


        fps = cv2.getTickFrequency()/(cv2.getTickCount()-timer)
        cv2.putText(self.img, str(int(fps)), (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

        cv2.imshow("track", self.img)

        print("IN camera process")

    def drawbox(self):
        x,y,w,h = int(self.bbox[0]),int(self.bbox[1]),int(self.bbox[2]),int(self.bbox[3])
        cv2.rectangle(self.img,(x,y),((x+w),(y+h)),(255,0,10),3,1)


def main():
    process = processing()

    while True:
        process.camera_process()

        k = cv2.waitKey(1)
        if k == ord("q"):
            return


if __name__ == "__main__":
    main()
