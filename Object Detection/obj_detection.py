import cv2
import numpy as np


detector = cv2.SIFT
FLANN_INDEX_KDTREE = 0
flannParam = dict(alogorith = FLANN_INDEX_KDTREE, tree = 0)

flann = cv2.FlannBasedMatcher(flannParam, {})

trainImg = cv2.imread( "C:/Users/Harshid/Desktop/Object Detection/Training/2020-04-03-22.36.13_frame_1/tiff", 0)
trainKP, trainDecs = detector.detectAndCompute(trainingImg , None )

det