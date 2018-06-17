import matplotlib.pyplot as plt 
import cv2
import time
import numpy as np

detector=cv2.SimpleBlobDetector_create()
im=cv2.imread('C:\\Users\\user\\Desktop\\python image\\color.jpg')
im=cv2.resize(im,(400,400))
#im_gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
keypoint=detector.detect(im)
blank=np.zeros((1,1))
#output1=cv2.drawKeypoints(im,keypoint,blank,(0,255,70),cv2.DRAW_MATCHES_FLAGS_DEFAULT)
#output2=cv2.drawKeypoints(im,keypoint,blank,(20,255,70),cv2.DRAW_MATCHES_FLAGS_NOT_DRAW_SINGLE_POINTS)
#output3=cv2.drawKeypoints(im,keypoint,blank,(40,255,70),cv2.DRAW_MATCHES_FLAGS_DRAW_OVER_OUTIMG)
output4=cv2.drawKeypoints(im,keypoint,blank,(60,255,70),cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
#cv2.imshow('blob etection one',output1)
#cv2.imshow('blob etection two',output2)
#cv2.imshow('blob etection three',output3)
cv2.imshow('blob etection four',output4)
cv2.waitKey()
cv2.destroyAllWindows()



