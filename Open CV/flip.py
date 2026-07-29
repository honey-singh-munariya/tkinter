import cv2
img = cv2.imread("Open CV/OIP.webp")

weidth = 400
height = 400

dim = (weidth,height)

resized = cv2.resize(img, dim)

cv2.imshow("img", resized)

disp = cv2.flip(resized,1)

cv2.imshow("display", disp)
time = cv2.waitKey(0)
cv2.waitKey(0)

cv2.destroyAllWindows()