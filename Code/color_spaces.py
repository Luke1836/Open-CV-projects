import cv2 as cv
import numpy as np

img = cv.imread("Resources/Images/nyiragonga.jpg")
img_resize = cv.resize(img, (1300,400), interpolation=cv.INTER_CUBIC)
blank = np.zeros(img_resize.shape[:2], dtype='uint8')
img_rgb = cv.cvtColor(img_resize, cv.COLOR_BGR2RGB)
cv.imshow("RGB", img_rgb)
cv.imshow("Nyiragonga", img_resize)

b,g,r = cv.split(img_resize)
blue = cv.merge([b, blank, blank])
red = cv.merge([blank, blank, r])
green = cv.merge([blank, g, blank])
cv.imshow("Blue", blue)
cv.imshow("Red", red)
cv.imshow("Green", green)
cv.waitKey(0)