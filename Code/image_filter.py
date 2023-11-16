import cv2 as cv

img = cv.imread("Resources/Photos/park.jpg")

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

blur = cv.blur(img, (3,3), cv.BORDER_DEFAULT)
cv.imshow('Blurred image', blur)

canny = cv.Canny(img,125,176)
cv.imshow('Canny', canny)

crop = img[120:350, 200:450]
cv.imshow('Crop', crop)

dilated = cv.dilate(img, (3,3), iterations=5)
cv.imshow('Dilated', dilated)
cv.waitKey(0)