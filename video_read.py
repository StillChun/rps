import cv2

video = cv2.VideoCapture('./test_video.mp4') #if argument is '0', camera will take a video

fourcc = cv2.VideoWriter_fourcc('D', 'I', 'V', 'X')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (1920,816))

while(video.isOpened()):
    ret, frame = video.read()

    if ret:
        out.write(frame)
        cv2.imshow('frame', frame)
    else:
        break

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
out.release()
cv2.destroyAllWindows()