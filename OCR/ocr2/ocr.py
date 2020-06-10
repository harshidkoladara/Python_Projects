def main():

    import numpy as np

    import cv2

    import imutils

    import sys

    import pytesseract

    import pandas as pd

    import time
    import os
# #     import glob

# #     path = glob.glob("/home/Rajn/Desktop/Output/*.jpg")
# #     cv2_img = []
# #     for img in path:
# #         n = cv2.imread(img)
# #         cv2_img.append(n)
# Add this line to assert the path. Else TesseractNotFoundError will be raised.

# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
#pytesseract.pytesseract.tesseract_cmd = r"./usr/bin/tesseract"

# Read the original image.

#     img = cv2.imread("1.jpg")
#     listing = os.listdir(r'/home/suzen/Desktop/Output/')
#     for img1 in listing:
#         #img1 = r"/home/suzen/Desktop/Output/"+img1
#         img = cv2.imread(img1)


# Using imutils to resize the image.
    img = cv2.imread('C:/Users/Harshid/Desktop/dv/python/ocr2/demo.png')
    img = imutils.resize(img, width=500)
    print("1")

    cv2.imshow("Original Image", img)  # Show the original image

    cv2.waitKey(0)
    print("2")

    # Convert from colored to Grayscale.

    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    print("3")

    # Show modification.
    cv2.imshow("Preprocess 1 - Grayscale Conversion", gray_img)

    cv2.waitKey(0)

    gray_img = cv2.bilateralFilter(gray_img, 11, 17, 17)

    # Showing the preprocessed image.
    cv2.imshow("Preprocess 2 - Bilateral Filter", gray_img)

    cv2.waitKey(0)

    # Finding edges of the grayscale image.

    c_edge = cv2.Canny(gray_img, 170, 200)

    # Showing the preprocessed image.
    cv2.imshow("Preprocess 3 - Canny Edges", c_edge)

    cv2.waitKey(0)

    # Finding contours based on edges detected.

    cnt, new = cv2.findContours(c_edge, cv2.RETR_LIST , cv2.CHAIN_APPROX_NONE)

    # Storing the top 30 edges based on priority

    print(len(cnt))
    cnt = sorted(cnt, key=cv2.contourArea, reverse=True)
    

    NumberPlateCount = None

    im2 = img.copy()

    cv2.drawContours(im2, cnt, -1, (0, 255, 0), 3)

    cv2.imshow("Top 30 Contours", im2)  # Show the top 30 contours.

    cv2.waitKey(0)

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

    cv2.waitKey(0)

    # Configuration for tesseract

    configr = ('-l eng --oem 1 --psm 3')

    # Running Tesseract-OCR on final image.

    text_no = pytesseract.image_to_string(new_image)
    print(text_no)
    # The extracted data is stored in a data file.

    data = {'Date': [time.asctime(time.localtime(time.time()))],

            'Vehicle_number': [text_no]}

    df = pd.DataFrame(data, columns=['Date', 'Vehicle_number'])

    df.to_csv('C:/Users/Harshid/Desktop/dv/python/ocr2/Dataset_VehicleNo.csv')

    # Printing the recognized text as output.

    

    cv2.waitKey(0)


if __name__ == '__main__':

    main()

