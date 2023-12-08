import cv2 as cv
import numpy as np

img = cv.imread("Resources/Photos/cats.jpg")
img_resize = cv.resize(img, (1000,600), interpolation=cv.INTER_AREA)
blank = np.zeros((img_resize.shape[:2]), dtype='uint8')

rectangle = cv.rectangle(blank.copy(), (img_resize.shape[1]//2 - 350,img_resize.shape[0]//2 - 200), (img_resize.shape[1]//2 + 350,img_resize.shape[0]//2 + 200), (255,255,255), thickness=-1)
circle = cv.circle(blank.copy(), (img_resize.shape[1]//2, img_resize.shape[0]//2), 250, 255, thickness=-1)
mask_shape = cv.bitwise_or(rectangle, circle)
masked = cv.bitwise_and(img_resize, img_resize, mask=mask_shape)
cv.imshow('Mask', mask_shape)
cv.imshow('Masked', masked)
cv.waitKey(0)
