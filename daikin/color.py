import cv2
import numpy as np

img = cv2.imread('/Users/i037762/Downloads/Baidu/materials/tong.png')

# set color thresh
#lower=np.array([165,130,76])
#upper=np.array([180,148,96])
lower=np.array([76,130,165])
upper=np.array([96,148,180])
# change to hsv model
#hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# get mask
mask = cv2.inRange(img, lower, upper)
cv2.imshow('Mask', mask)

# detect blue
res = cv2.bitwise_and(img, img, mask=mask)
cv2.imshow("images", np.hstack([img, res]))
cv2.waitKey(0)
if (res.max()>0):
    print('The picture contains copper pipe!')


#铜 169,139,83， max=169 min=83  V=169， s=86/169*60=30.5 H=56/86*60=39