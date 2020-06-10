import cv2

# Load an color image in color
img = cv2.imread('demo.jpeg',1)
print(img)

# Load an color image in grayscale
img = cv2.imread('demo.jpeg',0)
print(img)

# Load an color image in unchanged
img = cv2.imread('demo.jpeg',-1)
print(img)