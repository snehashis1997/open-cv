#import library
import matplotlib.pyplot as plt 
import cv2
import time
import numpy as np

#video capture
cap=cv2.VideoCapture(0)
while cap.isOpened():
    ret,frame=cap.read()
    frame_gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    frame_blur=cv2.GaussianBlur(frame_gray,(5,5),0)
    canny_edge=cv2.Canny(frame_blur,60,250)
    ret,mask=cv2.threshold(canny_edge,90,255,cv2.THRESH_BINARY_INV)
    cv2.imshow('edge detection',mask)
    if (cv2.waitKey(1)==ord('q')):
         break
cap.release()
cv2.destroyAllWindows()
