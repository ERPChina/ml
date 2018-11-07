import numpy as np
import threading
import time
import cv2
from PIL import Image
import detection as ml
import queue


def produce():
    while(True): # 从摄像头中读取画面，while表示循环读取画面，也就是一张一张图片形成了一个视频
        ret, image = cap.read() # 设置每一张图片的颜色

        img_color = cv2.cvtColor(image, 0) # 显示窗口
        #cv2.imshow('window', img_color)
        #img_color=cv2.putText(img_color,str(i),(50,200),cv2.FONT_HERSHEY_SIMPLEX,1.2,(255,0,0),5)
        q.put(img_color,True)
        time.sleep(5)

def consume():
    img_color=q.get(True)
    img_result=ml.detectBinaryImage( Image.fromarray(cv2.cvtColor(img_color,cv2.COLOR_BGR2RGB)))
    img_show = cv2.cvtColor(np.asarray(img_result),cv2.COLOR_RGB2BGR)
    #cv2.imshow('window', img_show) # 如果按下键盘上的 Q 就关闭窗口
    q.task_done()
    result.put(img_show,True)
    #time.sleep(3)

cap = cv2.VideoCapture(0)
#fps = cap.get(cv2.CAP_PROP_FPS)
threads = []
q = queue.Queue()
result=queue.Queue()
t1 = threading.Thread(target=produce)
threads.append(t1)
t2 = threading.Thread(target=consume)
threads.append(t2)
for t in threads:
    t.setDaemon(True)
    t.start()

while(True):
    if not result.empty():
        final_img=result.get(True)
        cv2.imshow('Video Camera Monitor', final_img)
        result.task_done()
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break;
cap.release()
cv2.destroyAllWindows()
