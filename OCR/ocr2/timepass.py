import numpy as np
import cv2
import imutils
import sys
import pytesseract
import pandas as pd
import time
import datetime
import os
import threading

(camx, camy) = (320, 240)
cap = cv2.VideoCapture(0)
cap.set(3, camx)
cap.set(4, camy)


def capture():
    try:
        while True:
            ret, frame = cap.read()
            cv2.imshow("OCR", frame)

            key = cv2.waitKey(1)
            if key == 27:
                cap.release()
                cv2.destroyAllWindows()

            elif key == ord('q'):
                filename = "C:/Users/Harshid/Desktop/dv/python/ocr2/" + \
                    datetime.datetime.now().strftime("%Y-%m-%d-%H.%M.%S_frame_" + str(1)+".tiff")
                cv2.imwrite(filename, frame)
                image_process_thread1 = threading.Thread(
                    target=image_process, args=(filename, ))
                image_process_thread1.start()

                time.sleep(0.1)
                filename = "C:/Users/Harshid/Desktop/dv/python/ocr2/" + \
                    datetime.datetime.now().strftime("%Y-%m-%d-%H.%M.%S_frame_" + str(2)+".tiff")
                cv2.imwrite(filename, frame)
                image_process_thread2 = threading.Thread(
                    target=image_process, args=(filename, ))
                image_process_thread2.start()
    except Exception as e:
        print(f' \n\n\n\n\n {e} ')


def image_process(filename):
    print(filename)
    img = cv2.imread(filename)
    # Convert from colored to Grayscale.

    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # thres_frame = cv2.adaptiveThreshold(
    #     gray_img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 299, 5)

    # result = pytesseract.image_to_string(thres_frame)

    # data = {'Date': [time.asctime(time.localtime(time.time()))],

    #         'Vehicle_number': [result]}

    # print(result)
    # key = cv2.waitKey(1)
    # if key == ord('p'):
    #     cap.release()
    #     cv2.destroyAllWindows()
    #     return


if __name__ == "__main__":
    record_thead = threading.Thread(target=capture)
    record_thead.start()
