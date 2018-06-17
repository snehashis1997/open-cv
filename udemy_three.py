import matplotlib.pyplot as plt 
import cv2
import time
import numpy as np

"""path1='C:\\Users\\user\\Desktop\\python image\\i1.jpg'
path2='C:\\Users\\user\\Desktop\\python image\\i2.jpg'

im1=cv2.imread(path1)
im2=cv2.imread(path2)

im1=cv2.resize(im1,(400,400))
im2=cv2.resize(im2,(400,400))

hei1,width1=im1.shape[:2]
hei2,width2=im2[:2]


q_hei1=hei1/4
q_width1=width1/4

im4=cv2.add(im1,im2)
im5=cv2.subtract(im1,im2)
cv2.imwrite('cpim1.jpg',im4)

t=np.array([[1,0,q_width1],[0,1,q_hei1]])
rotation_matrix=cv2.getRotationMatrix2D((q_width1,q_hei1),30,2)
rotation_matrix_im1=cv2.warpAffine(im1,rotation_matrix,(width1,hei1))

im1_tra=cv2.warpAffine(im1,t,(width1,hei1))
im1_transpose=cv2.transpose(im1)

cv2.imshow('1st',im4)
cv2.waitKey()

cv2.imshow('2nd',rotation_matrix_im1)
cv2.waitKey()

cv2.imshow('3rd',im1_transpose)
cv2.waitKey()"""
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
