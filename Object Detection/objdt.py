import cv2
import numpy as np

detector = cv2.xfeatures2d.SIFT_create()
FLANN_INDEX_KDTREE = 0
flannParam = dict(algotithm = FLANN_INDEX_KDTREE, tree = 5)
flann = cv2.FlannBasedMatcher(flannParam, {})

trainImg = cv2.imread("C:/Users/Harshid/Desktop/Object Detection/Training/2020-04-03-22.37.01_frame_1.tiff", 0)
trainKP, trainDecpa = detector.detectAndCompute()
