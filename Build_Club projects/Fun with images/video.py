import cv2 as cv

capture = cv.VideoCapture(0)
width = capture.get(cv.CAP_PROP_FRAME_WIDTH)
height = capture.get(cv.CAP_PROP_FRAME_HEIGHT)
fps = capture.get(cv.CAP_PROP_FPS)

print(f'Width: {width}\nHeight: {height}\nFrames per second: {fps}\n')
haar_cascade = cv.CascadeClassifier('C:/Users/georg/OneDrive/Desktop/Programming/Open CV/Code/haar_cascade.xml')
while True:
    isTrue, frames = capture.read()
    cv.imshow('Video', frames)
    if(cv.waitKey(20) & 0xFF == ord('d')):
        break

capture.release()
cv.destroyAllWindows()