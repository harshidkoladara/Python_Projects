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
    

    # Show modification.
    cv2.imshow("Preprocess 1 - Grayscale Conversion" + filename, gray_img)
    # time.sleep(10)

    gray_img = cv2.bilateralFilter(gray_img, 11, 17, 17)

    # Showing the preprocessed image.
    cv2.imshow("Preprocess 2 - Bilateral Filter"+ filename, gray_img)


    # Finding edges of the grayscale image.

    c_edge = cv2.Canny(gray_img, 170, 200)

    # Showing the preprocessed image.
    cv2.imshow("Preprocess 3 - Canny Edges"+ filename, c_edge)
    print(2)

    # Finding contours based on edges detected.

    cnt, new = cv2.findContours(c_edge, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

    # Storing the top 30 edges based on priority

    cnt = sorted(cnt, key=cv2.contourArea, reverse=True)[:30]

    NumberPlateCount = None

    im2 = img.copy()

    cv2.drawContours(im2, cnt, -1, (0, 255, 0), 3)

    cv2.imshow("Top 30 Contours", im2)  # Show the top 30 contours.

    count = 0

    for c in cnt:

        perimeter = cv2.arcLength(c, True)  # Getting perimeter of each contour

        approx = cv2.approxPolyDP(c, 0.02 * perimeter, True)

        if len(approx) == 4:  # Selecting the contour with 4 corners/sides.

            NumberPlateCount = approx

        break

    '''A picture can be stored as a numpy array. Thus to mask the unwanted portions of the

        picture, we simply convert it to a zeros array.'''

    # Masking all other parts, other than the number plate.

    masked = np.zeros(gray_img.shape, np.uint8)

    new_image = cv2.drawContours(masked, [NumberPlateCount], 0, 255, -1)

    new_image = cv2.bitwise_and(img, img, mask=masked)

    # The final image showing only the number plate.
    cv2.imshow("4 - Final_Image", new_image)


    # Configuration for tesseract

    configr = ('-l eng --oem 1 --psm 3')

    # Running Tesseract-OCR on final image.

    text_no = pytesseract.image_to_string(new_image)

    # The extracted data is stored in a data file.

    data = {'Date': [time.asctime(time.localtime(time.time()))],

            'Vehicle_number': [text_no]}

    df = pd.DataFrame(data, columns=['Date', 'Vehicle_number'])

    df.to_csv('Dataset_VehicleNo.csv')

    # Printing the recognized text as output.

    print(10)
    print(text_no)
    key = cv2.waitKey(1)
    if key == ord('p'):
        cap.release()
        cv2.destroyAllWindows()
        return    



if __name__ == "__main__":
    record_thead = threading.Thread(target=capture)
    record_thead.start()
