import os
import cv2
import numpy as np
import imutils
import sys
import pytesseract
import pandas as pd
import time
from datetime import date


def main():
    pathOut = r"C:/Users/Harshid/Desktop/tensor"
    count = 0
    counter = 1
    listing = os.listdir(r'C:/Users/Harshid/Desktop/tensor')
    fnames = []
    global data_list
    df = pd.DataFrame(columns=['Date', 'Vehicle_number', 'Place'])
    data_list = list()
    for vid in listing:
        vid = r"C:/Users/Harshid/Desktop/tensor/ass.webm"
        cap = cv2.VideoCapture(vid)
        count = 0
        counter += 1
        success = True
        while success:
            success, image = cap.read()
            print('read a new frame:', success)
            if count % 30 == 0:
                fname = 'frame{0}.jpg'.format(count)
                print(fname, 'xxxxxx')
                if fname != 'frame0.jpg':
                    fnames.append(fname)
                    cv2.imwrite(pathOut + fname, image)
                    #processImage('/home/suzen/Desktop/Output/' + fname)
            count += 1

    for i in fnames:
        processImage('C:/Users/Harshid/Desktop/tensor' + i)
    else:
        for data in data_list:
                df = df.append(data, ignore_index=True)
        df.to_csv('C:/Users/Harshid/Desktop/tensor/Dataset_VehicleNo.csv')


def processImage(imgname):
    img = cv2.imread(imgname)
    img = imutils.resize(img, width=500)
    #cv2.imshow("Original Image", img)
    # cv2.waitKey(0)
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #cv2.imshow("Preprocess 1 - Grayscale Conversion", gray_img)
    # cv2.waitKey(0)
    gray_img = cv2.bilateralFilter(gray_img, 11, 17, 17)
    #cv2.imshow("Preprocess 2 - Bilateral Filter", gray_img)
    # cv2.waitKey(0)
    c_edge = cv2.Canny(gray_img, 170, 200)
    #cv2.imshow("Preprocess 3 - Canny Edges", c_edge)
    # cv2.waitKey(0)
    cnt, new = cv2.findContours(c_edge, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    cnt = sorted(cnt, key=cv2.contourArea, reverse=True)[:30]
    NumberPlateCount = None
    im2 = img.copy()
    cv2.drawContours(im2, cnt, -1, (0, 255, 0), 3)
    # cv2.imshow("Top 30 Contours", im2)  # Show the top 30 contours.
    # cv2.waitKey(0)
    count = 0
    for c in cnt:
        perimeter = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.02 * perimeter, True)
        if len(approx) == 4:  # Selecting the contour with 4 corners/sides.
            NumberPlateCount = approx
        break
        # new line
    masked = np.zeros(gray_img.shape, np.uint8)
    new_image = cv2.drawContours(masked, [NumberPlateCount], 0, 255, -1)
    new_image = cv2.bitwise_and(img, img, mask=masked)
    # cv2.imshow("4 - Final_Image", new_image)
    # cv2.waitKey(0)
    configr = ('-l eng --oem 1 --psm 3')
    text_no = pytesseract.image_to_string(new_image)
    data = {'Date': [date.today()], 'Vehicle_number': [text_no], 'Place' : ['Paldi']}
    data_list.append(data)

    print(text_no, 'yyyyyyyyyy')
    cv2.waitKey(0)


if __name__ == '__main__':
    main()
