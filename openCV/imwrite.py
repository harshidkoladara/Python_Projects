import cv2

img = cv2.imread('demo.jpeg',0)
cv2.imshow('image',img)
cv2.imwrite('new.png',img)
img2 = cv2.imread('new.png', 0)
cv2.imshow('img2', img2)
print("Image stored in a working Directory")
cv2.waitKey(0)
cv2.destroyAllWindows()