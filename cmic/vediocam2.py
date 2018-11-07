import numpy as np
import cv2
from PIL import Image
import yolo as ml


cap = cv2.VideoCapture(0)
while(True): # 从摄像头中读取画面，while表示循环读取画面，也就是一张一张图片形成了一个视频
    ret, image = cap.read() # 设置每一张图片的颜色
    img_color = cv2.cvtColor(image, 0) # 显示窗口
        #cv2.imshow('window', img_color)
    #img_color=cv2.putText(img_color,str(i),(50,200),cv2.FONT_HERSHEY_SIMPLEX,1.2,(255,0,0),5)
    #img_result=ml.detectBinaryImage( Image.fromarray(cv2.cvtColor(img_color,cv2.COLOR_BGR2RGB)))
    #img_show = cv2.cvtColor(np.asarray(img_result),cv2.COLOR_RGB2BGR)
    img_result=ml.detection(cv2.cvtColor(img_color,cv2.COLOR_BGR2RGB))
    cv2.imshow('window', img_result) # 如果按下键盘上的 Q 就关闭窗口
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break;
cap.release()
cv2.destroyAllWindows()
