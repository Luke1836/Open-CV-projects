import cv2 as cv

def rescale(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

img = cv.imread("Resources\Photos\cat_large.jpg")
img_resize = rescale(img, scale=0.50)
cv.imshow('Cat', img_resize)
cv.waitKey(0)

#Video capturing and displaying
capture = cv.VideoCapture("Resources/Videos/dog.mp4")
while True:
    isTrue, frame = capture.read()
    frame_resize = rescale(frame, scale=0.50)
    cv.imshow('Video', frame_resize)
    if(cv.waitKey(20) & 0xFF == ord('d')):
        break
capture.release()
cv.destroyAllWindows()
cv.waitKey(0)


