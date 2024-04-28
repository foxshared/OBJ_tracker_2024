# Improve code structure using class

import cv2
import numpy as np


class processing():
    def __init__(self):

        self.camera_cap = cv2.VideoCapture(1)
        # self.tracker = cv2.TrackerKCF_create()
        self.flag = 0
        self.tracker = cv2.TrackerCSRT_create()
        for x in range(0, 5):
            success, self.img = self.camera_cap.read()
            print("OK {}" .format(x))
            success = success
            self.img = self.img

        self.bbox = cv2.selectROI("track", self.img, False)
        self.tracker.init(self.img, self.bbox)

        self.filename = 'savedImage.jpg'


        cv2.imwrite(self.filename, self.img)
        self.last_bbox = self.bbox

        self.camera_process()

    def camera_process(self):
        while True:
            timer = cv2.getTickCount()
            success, self.img = self.camera_cap.read()
            _,self.raw_img = self.camera_cap.read()
            
            success, self.bbox = self.tracker.update(self.img)
            if success:
                self.drawbox()
                cv2.putText(self.img, "Track", (10, 70),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
            else:
                cv2.putText(self.img, "Loss", (10, 70),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

            fps = cv2.getTickFrequency()/(cv2.getTickCount()-timer)
            cv2.putText(self.img, str(int(fps)), (10, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
            
            

            k =cv2.waitKey(1)
            if k == ord("q"):
                break

            if k == ord("i"): # Press "i" MANUAL REINIT BUTTON
                # bbox = cv2.selectROI("track",img,False)
                # print(bbox)

                memory_img = cv2.imread(self.filename,cv2.IMREAD_COLOR)
                self.tracker.init(memory_img, self.last_bbox)
                print("done init")

            if k == ord("k"):
                cv2.imwrite(self.filename, self.raw_img)
                self.last_bbox = self.bbox
                print("done save")

            cv2.imshow("track", self.img)
            # cv2.imshow("raw_cap",self.raw_img)

            print("IN camera process {b1}=={b2}".format(
                b1=self.last_bbox, b2=self.bbox))

    def drawbox(self):
        x, y, w, h = int(self.bbox[0]), int(
            self.bbox[1]), int(self.bbox[2]), int(self.bbox[3])
        cv2.rectangle(self.img, (x, y), ((x+w), (y+h)), (255, 0, 10), 3, 1)


def main():
    process = processing()


if __name__ == "__main__":
    main()
