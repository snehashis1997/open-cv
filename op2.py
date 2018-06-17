#import library 
import matplotlib.pyplot as plt 
import cv2
import time
import numpy as np

#import image 
path1='C:\\Users\\user\\Desktop\\python image\\i1.jpg'
path2='C:\\Users\\user\\Desktop\\python image\\i2.jpg'

i1=cv2.imread(path1)
i2=cv2.imread(path2)
i1=cv2.resize(i1,(500,500))
i2=cv2.resize(i2,(500,500))

for i in np.linspace(0,1,100):
	alpha=i
	beta=1-alpha
	output=cv2.addWeighted(i1,alpha,i2,beta,0)
	cv2.imshow('transition',output)
	time.sleep(.5)
	if cv2.waitKey(1)==27:
		break
cv2.destroyAllWindows()



