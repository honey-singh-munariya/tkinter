# Importing the modules...
import cv2

# giving the path and the color of the values...
img = cv2.imread("C:/Users/honey/OneDrive/Desktop/Open CV/OIP.webp",0)

# print the size of the image...
print("The size of the image", img.shape)

#To resize the shape...
width = 1000
height= 700
dim = (width,height)
resized = cv2.resize(img, dim)

# showing the image...
cv2.imshow('window', resized)

# writing the image...
cv2.imwrite("car.jpg", img)

# show timing limit of the image...
cv2.waitKey(100000)

# close all the windows...
cv2.destroyAllwindows()



