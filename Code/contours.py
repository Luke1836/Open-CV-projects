#python3
import cv2 as cv

img = cv.imread("Resources/Photos/cats.jpg")
img_resize = cv.resize(img, (1000,600), interpolation=cv.INTER_AREA)
canny = cv.Canny(img_resize, 125, 175)
gray = cv.cvtColor(img_resize, cv.COLOR_BGR2GRAY)
""" contours, hierachies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)

print(f'{len(contours)} contours found!') """
ret, thresh = cv.threshold(gray, 125,255,cv.THRESH_BINARY)
cv.imshow('Thresh', thresh)

contours, hierachies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contours found!')

cv.imshow('Cats', img_resize)
cv.imshow('Canny', canny)
cv.waitKey(0)