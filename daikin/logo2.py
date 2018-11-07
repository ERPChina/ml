import sys
import cv2
import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    # If image path and f/q is not passed as command
    # line arguments, quit and display help message
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(1)

    # speed-up using multithreads
    cv2.setUseOptimized(True);
    cv2.setNumThreads(4);

    # read image
    im = cv2.imread(sys.argv[1])
    im= cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)#灰度图像
    # resize image
    #newHeight = 200
    #newWidth = int(im.shape[1]*200/im.shape[0])
    #im = cv2.resize(im, (newWidth, newHeight))
    logo=cv2.imread(sys.argv[2])
    logo= cv2.cvtColor(logo,cv2.COLOR_BGR2GRAY)#灰度图像
    w, h = logo.shape[::-1]
    res = cv2.matchTemplate(im,logo,cv2.TM_CCOEFF_NORMED)#设定阈值
    loc = np.where( res >= 0.4)
    for pt in zip(*loc[::-1]):
        cv2.rectangle(im, pt, (pt[0] + w, pt[1] + h), (7,249,151), 2) #显示图像
    cv2.imshow('Detected',im)
    k = cv2.waitKey(0)

