import numpy as np
import cv2
cap=cv2.VideoCapture(0)
if cap.isOpened():
    ret,frame = cap.read()
else:
    ret = False
while(ret):
  ret,frame=cap.read()
  gray_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
  edges=cv2.Canny(gray_frame,50,150,apertureSize = 3,L2gradient = True)
  lines = cv2.HoughLines(edges,1,np.pi/180,200)
  
  if lines is not None:
      for rho,theta in lines[0]:
          a = np.cos(theta)
          b = np.sin(theta)
          x0 = a*rho
          y0 = b*rho
          pt1 = (int(x0+1000*(-b)),int(y0+1000*(-a)))
          pt2 = (int(x0-1000*(-b)),int(y0-1000*(-a)))
          cv2.line(frame,pt1,pt2,(0,255,00),2)       
         
  cv2.imshow("output",frame)
  if cv2.waitKey(1) == 27:
      break
  
cap.release()
cv2.destroyAllWindows()
