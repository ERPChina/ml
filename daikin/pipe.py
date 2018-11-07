import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('/Users/i037762/Downloads/Baidu/materials/qiang3.png')


grey = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)#灰度图像

#plt.subplot(121),plt.imshow(grey,'gray')
#open to see how to use: cv2.Canny
#http://blog.csdn.net/on2way/article/details/46851451
#edges = cv2.Canny(grey,20,60)

#circle detection
img2=cv2.bilateralFilter(grey, 10, 40, 10)
plt.subplot(121),plt.imshow(img2,'gray')
#circles=cv2.HoughCircles(img2,cv2.HOUGH_GRADIENT,1,100,param1=210,param2=70,minRadius=100,maxRadius=300)
#parameter for 穿墙的空进行检测
circles=cv2.HoughCircles(img2,cv2.HOUGH_GRADIENT,2,100,param1=120,param2=40,minRadius=250,maxRadius=300)
circles = np.uint16(np.around(circles))
for i in circles[0,:]:
    # draw the outer circle
    cv2.circle(img,(i[0],i[1]),i[2],(255,0,0),20)
plt.subplot(122),plt.imshow(img,'gray')
plt.xticks([]),plt.yticks([])
plt.show()
#hough transform
#lines = cv2.HoughLinesP(edges,1,np.pi/180,60,minLineLength=60,maxLineGap=10)
#lines1 = lines[:,0,:]#提取为二维
#for x1,y1,x2,y2 in lines1[:]:

#    cv2.line(img,(x1,y1),(x2,y2),(255,0,0),1)
#plt.subplot(122),plt.imshow(img,)
#plt.xticks([]),plt.yticks([])
