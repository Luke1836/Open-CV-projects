import cv2 as cv 
import numpy as np

img_1 = cv.imread("download.jpg")
img_2 = cv.imread("mount-vesuvius.jpg")
img_resize = cv.resize(img_1,(500,500), interpolation=cv.INTER_AREA)
img_2_resize = cv.resize(img_2,(500,500), interpolation=cv.INTER_CUBIC)

print(img_1.shape)
gray_1 = cv.cvtColor(img_resize, cv.COLOR_BGR2GRAY)
gray_2 = cv.cvtColor(img_2_resize, cv.COLOR_BGR2GRAY)

hori_1 = cv.vconcat([img_resize, img_2_resize])
hori_2 = cv.vconcat([gray_1, gray_2])
cv.imwrite("C:/Users/georg/OneDrive/Desktop/Build_Club/Task1/image1.jpg", hori_1)
cv.imwrite("C:/Users/georg/OneDrive/Desktop/Build_Club/Task1/image2.jpg", hori_2)

image1 = cv.imread("image1.jpg")
image2 = cv.imread("image2.jpg")
final = cv.hconcat([image1, image2])
final_resize = cv.resize(final, (600,600), interpolation=cv.INTER_CUBIC)
cv.imshow('final', final_resize)
cv.waitKey(0)
cv.destroyAllWindows()

""" import cv2 as cv 
import numpy as np

img_1 = cv.imread("download.jpg")
img_2 = cv.imread("mount-vesuvius.jpg")
img_resize = cv.resize(img_1, (500, 500), interpolation=cv.INTER_AREA)
img_2_resize = cv.resize(img_2, (500, 500), interpolation=cv.INTER_AREA)

print(img_1.shape)
gray_1 = cv.cvtColor(img_resize, cv.COLOR_BGR2GRAY)
gray_2 = cv.cvtColor(img_2_resize, cv.COLOR_BGR2GRAY)

hori_1 = np.concatenate([img_resize, img_2_resize], axis=1)
hori_2 = np.concatenate([gray_2, gray_1], axis=1)

final = np.concatenate([hori_1, hori_2], axis=0)  

cv.imshow('Concatenated Image', final)
cv.waitKey(0)
cv.destroyAllWindows() """
