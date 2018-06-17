import matplotlib.pyplot as plt 
import cv2
import time
import numpy as np

path='C:\\Users\\user\\Desktop\\python image\\color.png'
template=cv2.imread(path)
template_gray=cv2.cvtColor(template,cv2.COLOR_BGR2GRAY)
ret,mask=cv2.threshold(template_gray,127,255,0)
_,con_tem, hier_temp = cv2.findContours(mask,cv2.RETR_CCOMP,cv2.CHAIN_APPROX_SIMPLE)
n=len(con_tem)-1
con_tem=sorted(con_tem,key=cv2.contourArea,reverse=True)[:n]
templete_out=con_tem[1]
cap=cv2.VideoCapture(0)
while cap.isOpened():
    ret,frame=cap.read()
    frame_gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    ret1_gray,mask1_gray=cv2.threshold(frame_gray,127,255,0)
    _,con_target,hier_target=cv2.findContours(mask1_gray,cv2.RETR_CCOMP,cv2.CHAIN_APPROX_SIMPLE)
    for c in con_target:
    	match=cv2.matchShapes(c,templete_out,1,0.0)
    	if match<.15:
    		closet=c
    	else:
    		closet=[]

    output=cv2.drawContours(frame,closet,-1,(0,52,220),3)
    cv2.imshow('output',output)
cap.release()
cv2.destroyAllWindows()






