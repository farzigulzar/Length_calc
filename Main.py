import cv2
import numpy as np
cap=cv2.VideoCapture(0)
i=0

frame=np.zeros((400,400,400),np.uint8)


while(i<60):

    i=i+1
    _, frame = cap.read()
    cv2.imshow('Video', frame)







    if (cv2.waitKey(1)==27):
        break

cap.release()
cv2.destroyAllWindows()