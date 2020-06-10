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
pinchFlag = 0
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

    if(len(conts) == 2):
        if(pinchFlag == 1):
            pinchFlag = 0
            mouse.release(Button.left)
        x1, y1, w1, h1 = cv2.boundingRect(conts[0])
        x2, y2, w2, h2 = cv2.boundingRect(conts[1])
        cv2.rectangle(img, (x1, y1), (x1+w1, y1+h1), (255, 0, 5), 2)
        cv2.rectangle(img, (x2, y2), (x2+w2, y2+h2), (255, 0, 0), 2)

        cx1 = x1+w1/2
        cy1 = y1+h1/2
        cx2 = x2+w2/2
        cy2 = y2+h2/2

        cx = (cx1+cx2)/2
        cy = (cy1+cy2)/2

        cv2.line(img, (int(cx1), int(cy1)),
                 (int(cx2), int(cy2)), (255, 0, 0), 2)
        cv2.circle(img, (int(cx), int(cy)), 2, (0, 0, 255), 2)

        mouseLoc = mLocOld+((int(cx), int(cy)) - mLocOld)/DumpingFactor
        mouseLock = (sx - ((mouseLoc[0]*sx)/camx), (mouseLoc[1]*sy)/camy)
        mouse.position = mouseLock
        # while mouse.position!=mouseLock:
        #     pass
        mLocOld = mouseLoc
        openx, opny, openw, openh = cv2.boundingRect(
            np.array([[[x1, y1], [x1+w1, y1+h1], [x2, y2], [x2+w2, y2+h2]]]))

    elif(len(conts) == 1):
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

    elif(len(conts) == 3):
        x1, y1, w1, h1 = cv2.boundingRect(conts[0])
        x2, y2, w2, h2 = cv2.boundingRect(conts[1])
        x3, y3, w3, h3 = cv2.boundingRect(conts[2])

        cv2.rectangle(img, (x1, y1), (x1+w1, y1+h1), (255, 0, 5), 2)
        cv2.rectangle(img, (x2, y2), (x2+w2, y2+h2), (255, 0, 0), 2)
        cv2.rectangle(img, (x3, y3), (x3+w3, y3+h3), (255, 0, 0), 2)

        cx1 = x1+w1/2
        cy1 = y1+h1/2
        cx2 = x2+w2/2
        cy2 = y2+h2/2
        cx3 = x3+w3/2
        cy3 = y3+h3/2

        cv2.line(img, (int(cx1), int(cy1)),
                 (int(cx2), int(cy2)), (255, 0, 0), 2)
        cv2.line(img, (int(cx2), int(cy2)),
                 (int(cx3), int(cy3)), (255, 0, 0), 2)
        cv2.line(img, (int(cx3), int(cy3)),
                 (int(cx1), int(cy1)), (255, 0, 0), 2)

        cx = (cx1+cx2+cx3)//3
        cy = (cy1+cy2+cy3)//3

        d1 = math.sqrt(math.pow(cx2 - cx1, 2) + math.pow(cy2 - cy1, 2)*1.0)
        d2 = math.sqrt(math.pow(cx3 - cx2, 2) + math.pow(cy3 - cy2, 2)*1.0)
        d3 = math.sqrt(math.pow(cx1 - cx3, 2) + math.pow(cy1 - cy3, 2)*1.0)

        d = (d1+d2+d3)/3
        cv2.circle(img, (int(cx), int(cy)), int(
            d/math.sqrt(3)), (0, 0, 244), 2)
        pinchFlag = 2    

    cv2.imshow("cam", img)
    cv2.imshow("cam", img)
    key = cv2.waitKey(1)
    if key == 27:
        cam.release()
        cv2.destroyAllWindows()
