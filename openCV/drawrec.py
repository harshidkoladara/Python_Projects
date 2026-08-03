import numpy as np
import cv2

# Create a black image
img = np.zeros((600,512,3), np.uint8)

img1= cv2.rectangle(img,(300,50),(200,150),(255,0,0),1)
cv2.imshow('image',img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
