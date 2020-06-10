import cv2 
import pytesseract
import os
import sys
import numpy as np


lower_white = np.array([0,0,168])
upper_white = np.array([172,111,255])
kernalOpen = np.ones((5, 5))
kernalClose = np.ones((20, 20))

img = cv2.imread("C:/Users/Harshid/Desktop/dv/python/ocr2/pqw.png")



# imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

#     # make mask
# mask = cv2.inRange(imgHSV, lower_white, upper_white)

# maskOpen = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernalOpen)
# maskClose = cv2.morphologyEx(maskOpen, cv2.MORPH_CLOSE, kernalClose)

# maskFinal = maskClose
# conts, h = cv2.findContours(
#         maskFinal.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

# print(len(conts))        

# counters = list()

# for x in conts:
#     x1, y1, w1, h1 = cv2.boundingRect(x)
#     counters.append([x1, y1, w1, h1])
# # x2, y2, w2, h2 = cv2.boundingRect(conts[1])

# for x in counters:
#     x1, y1, w1, h1 = x[0], x[1], x[2], x[3]
#     cv2.rectangle(img, (x1, y1), (x1+w1, y1+h1), (255, 0, 5), 2)
# # cv2.rectangle(img, (x2, y2), (x2+w2, y2+h2), (255, 0, 0), 2)        

# # text = pytesseract.image_to_string(mask)

# # print(mask)

# cv2.imshow("ocr", img)
# # cv2.imshow("imgHsv", imgHSV)
# # cv2.imshow("mask", mask)


key = cv2.waitKey(0)
if key == 27:
    cv2.destroyAllWindows()