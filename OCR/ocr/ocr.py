import numpy as np
import threading
import cv2
import sys
import os
import pytesseract
import time
from PIL import Image
import re

frame_count = 0
image_count = 0
delete_count = 0
# numberRE = re.compile(r'[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]')


array = []
lst = []


def capture():
    cap = cv2.VideoCapture(0)
    start_time = time.time()
    global frame_count

    try:
        while True:

            _, frame = cap.read()

            cv2.imshow("OCR", frame)

            gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # noise_reduce = np.ones((1, 1), np.uint8)
            # gray_frame = cv2.dilate(gray_frame, noise_reduce, iterations=1)
            # gray_frame = cv2.erode(gray_frame, noise_reduce, iterations=1)

            thres_frame = cv2.adaptiveThreshold(
                gray_frame, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 299, 5)

            cv2.imwrite("gray_frame_"+str(frame_count)+".png", thres_frame)
            frame_count += 1

            key = cv2.waitKey(1)
            if key == 27:
                cap.release()
                cv2.destroyAllWindows()

    except:
        print(
            f'Time running {time.time() - start_time} and images generated{frame_count}')
        print("destroyed..")


def recognized_text_set(args, counter):
    print(args)
    counter = args.split()
    counter = np.array(counter)
    array.append(counter)


def process_text(arr):
    arr_np = np.array(arr)
    i = arr_np.shape
    print("\n\n arr")
    # print(arr_np)
    for x in arr_np:
        for z in x:
            if z not in lst:
                lst.append(z)

    print("\n\n\n\n\n\n lst")
    print(lst)


def recognize_text():
    global image_count
    try:
        while True:
            if image_count <= frame_count:
                result = pytesseract.image_to_string(
                    Image.open("gray_frame_"+str(image_count)+".png"))

                # print("frame = "+str(image_count))

                recognized_text_set(result, 'lst'+str(image_count))
                image_count += 1

            else:
                break
    except:
        print(array)
        process_text(array)
        print("All frames are recognized")


def delete_frame():
    global delete_count
    try:
        while True:
            if(delete_count <= image_count):
                time.sleep(0.1)
                # print("removong "+"gray_frame_"+str(delete_count)+".png")
                os.remove("gray_frame_"+str(delete_count)+".png")
                delete_count += 1
    except:
        print("All frames are deleted")


if __name__ == "__main__":
    record_thread = threading.Thread(target=capture)
    record_thread.start()
    while frame_count == 0:
        pass
    recognize_thread = threading.Thread(target=recognize_text)
    recognize_thread.start()
    while image_count == 0:
        pass
    delete_thread = threading.Thread(target=delete_frame)
    delete_thread.start()
