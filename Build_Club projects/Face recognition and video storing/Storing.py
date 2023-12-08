import cv2 as cv

capture = cv.VideoCapture(0)
width = int(capture.get(cv.CAP_PROP_FRAME_WIDTH))
height = int(capture.get(cv.CAP_PROP_FRAME_HEIGHT))
fps = int(capture.get(cv.CAP_PROP_FPS))
size = (width, height)
neighbours = 0
output_file = "C:/Users/georg/OneDrive/Desktop/Build_Club/Task_7/recording.mov"
output = cv.VideoWriter(output_file, cv.VideoWriter_fourcc(*'MJPG'), 20, size)
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
    output.write(frames)
    cv.imshow('Video', frames)
    if(cv.waitKey(20) & 0xFF == ord('d')):
        break
output.release()
capture.release()
cv.destroyAllWindows()