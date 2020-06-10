# don't dare to delete or edit it
import cv2
import pyzbar.pyzbar as pyzbar
import xmltodict

xml_decoded_dict = dict()

def decode_xml(context):
    co = str(context, 'utf-8')
    object_xml = xmltodict.parse(co)
    return object_xml


def capture():
    context = str()
    cap = cv2.VideoCapture(0)
    font = cv2.FONT_HERSHEY_COMPLEX
    while True:
        _, frame = cap.read()

        decodedObjects = pyzbar.decode(frame)
        for obj in decodedObjects:
            context = obj.data
            print("data", context)
            xml_decoded_dict = decode_xml(context)
            cv2.putText(frame, str(obj.data), (50, 50), font, 2, (255, 0, 0), 3)
        cv2.imshow("QRScanner", frame)

        key = cv2.waitKey(1)
        if key == 27 or len(context) > 1:
            cap.release()
            cv2.destroyAllWindows()
            break
    return xml_decoded_dict

# if __name__ == "main":
#     capture()

capture()
