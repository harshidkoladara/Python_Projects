import cv2
import numpy as np
from pynput.mouse import Button, Controller
import wx
import math

mouse = Controller()

app = wx.App(False)
(sx, sy) = wx.GetDisplaySize()
(camx, camy) = (320, 240)


lowerBound = np.array([33, 80, 40])
upperBound = np.array([102, 255, 255])

cam = cv2.VideoCapture(0)
cam.set(3, camx)
cam.set(4, camy)
kernalOpen = np.ones((5, 5))
kernalClose = np.ones((20, 20))
mLocOld = np.array([0, 0])
mouseLoc = np.array([0, 0])
DumpingFactor = 2
openx, opny, openw, openh = (0, 0, 0, 0)

# font = cv2.cv.InitFont(cv2.cv.CV_FONT_HERSHEY_SIMPLEX, 2, 0.5, 0, 3, 1)

while True:
    ret, img = cam.read()
    # img = cv2.resize(img, (230, 220))

    # BGR TO HSV
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # make mask
    mask = cv2.inRange(imgHSV, lowerBound, upperBound)

    # morphology
    maskOpen = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernalOpen)
    maskClose = cv2.morphologyEx(maskOpen, cv2.MORPH_CLOSE, kernalClose)

    maskFinal = maskClose
    conts, h = cv2.findContours(
        maskFinal.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    if(len(conts) == 1):
        x, y, w, h = cv2.boundingRect(conts[0])

        # cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        cx = x+w/2
        cy = y+h/2
        cv2.circle(img, (int(cx), int(cy)), int((w+h)/4), (0, 0, 255), 2)

        mouseLoc = mLocOld+((int(cx), int(cy)) - mLocOld)/DumpingFactor
        mouseLock = (sx - ((mouseLoc[0]*sx)/camx), (mouseLoc[1]*sy)/camy)
        mouse.position = mouseLock
        # while mouse.position!=mouseLock:
        #     pass
        mLocOld = mouseLoc

    cv2.imshow("cam", img)
    key = cv2.waitKey(1)
    if key == 27:
        cam.release()
        cv2.destroyAllWindows()
