import cv2 as cv

capture = cv.VideoCapture(0)
width = capture.get(cv.CAP_PROP_FRAME_WIDTH)
height = capture.get(cv.CAP_PROP_FRAME_HEIGHT)
fps = capture.get(cv.CAP_PROP_FPS)
neighbours = 0

print(f'Width: {width}\nHeight: {height}\nFrames per second: {fps}\n')
haar_cascade = cv.CascadeClassifier('C:/Users/georg/OneDrive/Desktop/Programming/Open CV/Code/haar_cascade.xml')
while True:
    isTrue, frames = capture.read()
    faces_rect = haar_cascade.detectMultiScale(frames, 1.1, 5)
    if(neighbours != len(faces_rect)):
        neighbours = len(faces_rect)
        print(f'The number of neighbours found: {neighbours}')
    for (x,y,w,h) in faces_rect:
        cv.rectangle(frames, (x,y), (x+w, y+h), (0,255,0), thickness=2)
    cv.imshow('Video', frames)
    if(cv.waitKey(20) & 0xFF == ord('d')):
        break

capture.release()
cv.destroyAllWindows()