''' simple camera application based on OPEN CV2 module of python.'''
import cv2

video = cv2.VideoCapture(0)

while True:
    check,frame = video.read()
    print(frame,check)
    cv2.imshow("Cam",frame)
    key = cv2.waitKey(1)
    if key == ord('c'):
        cv2.imwrite('Capture.png',frame)
    elif key==ord('q'):
        break

video.release()
cv2.destroyAllWindows()
