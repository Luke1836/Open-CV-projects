import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype='uint8')

cv.rectangle(blank, (0,0), (blank.shape[1]//2,blank.shape[0]//2), (0,0,250), thickness=cv.FILLED)
cv.circle(blank, (blank.shape[1]//2,blank.shape[0]//2), 50, (120,0,0), thickness=cv.FILLED)
cv.line(blank, (10,10), (blank.shape[1]//2,blank.shape[0]//2), (250,250,250), thickness=2)
cv.putText(blank, "Destroyer King", (255,50), cv.FONT_HERSHEY_DUPLEX, 1.0, (222,222,245), thickness=2)
cv.imshow("Box", blank)
cv.waitKey(0)