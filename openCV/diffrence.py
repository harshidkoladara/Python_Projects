from PIL import Image ,ImageChops
img1=Image.open("11.jpg")
img2=Image.open("22.jpg")
diff=ImageChops.difference(img1,img2)
if diff.getbbox():
	diff.show()
