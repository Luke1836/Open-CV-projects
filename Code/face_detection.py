import cv2 as cv

img = cv.imread("Resources/Photos/lady.jpg")
cv.imshow("Face", img)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Face", gray)

haar_cascade = cv.CascadeClassifier('Code/haar_cascade.xml')
faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)
print(f'Number of neighbours found: {len(faces_rect)}')
""" Drawing Rectangle over the face borders """
for (x,y,w,h) in faces_rect:
    cv.rectangle(img, (x,y), (x+w, y+h), (0,255,0), thickness=2)
cv.imshow('Face detector', img)
cv.waitKey(0)