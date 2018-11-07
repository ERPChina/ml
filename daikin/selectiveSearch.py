import sys
import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage import measure as ms

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
    #im= cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)#灰度图像
    # resize image
    #newHeight = 200
    #newWidth = int(im.shape[1]*200/im.shape[0])
    #im = cv2.resize(im, (newWidth, newHeight))
    logo=cv2.imread(sys.argv[2])
    logo= cv2.cvtColor(logo,cv2.COLOR_BGR2GRAY)#灰度图像
    #plt.subplot(121),plt.imshow(im,'Greys')
    #plt.subplot(122),plt.imshow(logo,'Greys')
    # create Selective Search Segmentation Object using default parameters
    ss = cv2.ximgproc.segmentation.createSelectiveSearchSegmentation()

    # set input image on which we will run segmentation
    ss.setBaseImage(im)

    # Switch to fast but low recall Selective Search method
    if (sys.argv[3] == 'f'):
        ss.switchToSelectiveSearchFast()
    elif (sys.argv[3] == 's'):
        ss.switchToSingleStrategy()
    # Switch to high recall but slow Selective Search method
    elif (sys.argv[3] == 'q'):
        ss.switchToSelectiveSearchQuality()
    # if argument is neither f nor q print help message
    else:
        print(__doc__)
        sys.exit(1)

    # run selective search segmentation on input image
    rects = ss.process()
    print('Total Number of Region Proposals: {}'.format(len(rects)))

    # number of region proposals to show
    numShowRects = 100
    # increment to increase/decrease total number
    # of reason proposals to be shown
    increment = 50
    logoRatio=logo.shape[1]/logo.shape[0]


    # create a copy of original image
    imOut = im.copy()
    imRegion = im.copy()
    ims=imOut.copy()
    found = False

    # itereate over all the region proposals
    for i, rect in enumerate(rects):
        # draw rectangle for region proposal till numShowRects
        x, y, w, h = rect
        ratio=w/h
        cv2.rectangle(imRegion, (x, y), (x+w, y+h), (0, 255, 0), 1, cv2.LINE_AA)
        cv2.imshow('Proposal', imRegion)
        cv2.waitKey(5)
        if (abs(ratio-logoRatio)<0.1):

            crop_img = im[y:y+h, x:x+w]
            crop_img= cv2.cvtColor(crop_img,cv2.COLOR_BGR2GRAY)#灰度图像
            height,width = crop_img.shape[:2]
            logo2 = logo.copy()
            logo2=cv2.resize(logo2,(width, height))
            #res = cv2.matchTemplate(crop_img,logo,cv2.TM_CCOEFF_NORMED)#设定阈值
            #loc = np.where( res >= 0.8)

            cv2.rectangle(ims, (x, y), (x+w, y+h), (0, 255, 0), 1, cv2.LINE_AA)
            cv2.imshow('RatioFilter', ims)
            cv2.waitKey(5)

            img_template_probability_match = cv2.matchTemplate(crop_img, logo2, cv2.TM_CCOEFF_NORMED)[0][0]
            if(img_template_probability_match is not None):
                img_template_diff = 1 - img_template_probability_match
            if (img_template_diff is not None)&(img_template_diff<0.6):
                found=True
                cv2.rectangle(imOut, (x, y), (x+w, y+h), (0, 255, 0), 1, cv2.LINE_AA)
        else:
            continue

    # show output
    cv2.imshow('Output3', imOut)
    cv2.waitKey(5)
        # record key press
        #k = cv2.waitKey(500) & 0xFF

        # m is pressed
        #if k == 109:
            # increase total number of rectangles to show by increment
            #numShowRects += increment
        # l is pressed
        #elif k == 108 and numShowRects > increment:
            # decrease total number of rectangles to show by increment
            #numShowRects -= increment
        # q is pressed
        #else:
            #break
            # close image show window
    cv2.destroyAllWindows()
    if (found):
        print("this picture contains the logo of Daikin!")
