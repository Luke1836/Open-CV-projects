
import cv2 as cv

img_1 = cv.imread("download.jpg")
img_2 = cv.imread("mount-vesuvius.jpg")
img_resize = cv.resize(img_1,(400,400), interpolation=cv.INTER_AREA)
img_2_resize = cv.resize(img_2,(400,400), interpolation=cv.INTER_LINEAR)
cv.imshow("Mount Vesuvius", img_2_resize)

gray_1 = cv.cvtColor(img_resize, cv.COLOR_BGR2GRAY)
gray_2 = cv.cvtColor(img_2_resize, cv.COLOR_BGR2GRAY)
cv.imshow("Tom Cruise", img_resize)
cv.imshow("Gray", gray_1)
cv.imshow("Vesuvius_gray", gray_2)
cv.imwrite("C:/Users/georg/OneDrive/Desktop/Build_Club/Task1/gray.jpg",gray_1)
cv.imwrite("C:/Users/georg/OneDrive/Desktop/Build_Club/Task1/gray1.jpg",gray_2)


cv.waitKey(0)
cv.destroyAllWindows()
