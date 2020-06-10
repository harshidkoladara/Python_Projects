from pyzbar import pyzbar
import datetime
import imutils
import time
import cv2
from firebase import firebase


cap = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_COMPLEX
firebase = firebase.FirebaseApplication(
    'https://hacks-7da44.firebaseio.com/', None)
n = 0
while True:
    _, frame = cap.read()
    frame = imutils.resize(frame, width=400)

    barcodes = pyzbar.decode(frame)
    barcodeData = ''
    for barcode in barcodes:
        (x, y, w, h) = barcode.rect
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
        barcodeData = barcode.data.decode("utf-8")
        barcodeType = barcode.type

        text = "{} ({})".format(barcodeData, barcodeType)
        print(barcodeData)

    Final_Data = barcodeData
    if Final_Data == 'Lays':
        try:
            result_get = firebase.get('/hacks-7da44/Lays/', '')
            counter = result_get['Count']
            counter += 1
            lays_id = 'Lays' + str(counter)
            result = firebase.put('/hacks-7da44/Lays/', lays_id, text)
            result = firebase.put('/hacks-7da44/Lays/', 'Count', counter)
            print(result)
            break
        except:
            lays_id = 'Lays' + str(0)
            result = firebase.put('/hacks-7da44/Lays/', lays_id, text)
            result = firebase.put('/hacks-7da44/Lays/', 'Count', 0)
            break

    elif Final_Data == 'Pen':
        try:
            result_get = firebase.get('/hacks-7da44/Pen/', '')
            counter = result_get['Count']
            counter += 1
            Pen_id = 'Pen' + str(counter)
            result = firebase.put('/hacks-7da44/Pen/', Pen_id, text)
            result = firebase.put('/hacks-7da44/Pen/', 'Count', counter)
            print(result)
            break
        except:
            Pen_id = 'Pen' + str(0)
            result = firebase.put('/hacks-7da44/Pen/', Pen_id, text)
            result = firebase.put('/hacks-7da44/Pen/', 'Count', 0)
            print(result)
            break

    elif Final_Data == 'Nishita':
        try:
            result_get = firebase.get('/hacks-7da44/Nishita/', '')
            counter = result_get['Count']
            counter += 1
            nishita_id = 'Nishita' + str(counter)
            result = firebase.put('/hacks-7da44/Nishita/', nishita_id, text)
            result = firebase.put('/hacks-7da44/Nishita/', 'Count', counter)
            print(result)
            break
        except:
            nishita_id = 'Nishita' + str(0)
            result = firebase.put('/hacks-7da44/Nishita/', nishita_id, text)
            result = firebase.put('/hacks-7da44/Nishita/', 'Count', 0)
            print(result)
            break
    elif Final_Data == 'Specs':
        try:
            result_get = firebase.get('/hacks-7da44/Specs/', '')
            counter = result_get['Count']
            counter += 1
            speces_id = 'Specs' + str(counter)
            result = firebase.put('/hacks-7da44/Specs/', speces_id, text)
            result = firebase.put('/hacks-7da44/Specs/', 'Count', counter)
            print(result)
            break
        except:
            speces_id = 'Specs' + str(0)
            result = firebase.put('/hacks-7da44/Specs/', speces_id, text)
            result = firebase.put('/hacks-7da44/Specs/', 'Count', 0)
            print(result)
            break

    else:
        print("Invalid Product")

    cv2.imshow("QRScanner", frame)

    key = cv2.waitKey(1)
    if key == 27:
        cap.release()
        cv2.destroyAllWindows()
        break
