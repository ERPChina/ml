import cv2
import yolo as ml

#cap = cv2.VideoCapture(0)

cap = cv2.VideoCapture('/Volumes/NETAC/中集/违规作业/6 7/ch06_20181009151255.mp4')
while(True): # 从摄像头中读取画面，while表示循环读取画面，也就是一张一张图片形成了一个视频
    ret, image = cap.read() # 设置每一张图片的颜色
    image=cv2.resize(image, (512,384), interpolation=cv2.INTER_LINEAR)
    #img_color = cv2.cvtColor(image, 0) # 显示窗口
    #cv2.imshow('window', img_color)
    #img_color=cv2.putText(img_color,str(i),(50,200),cv2.FONT_HERSHEY_SIMPLEX,1.2,(255,0,0),5)
    #img_result=ml.detectBinaryImage( Image.fromarray(cv2.cvtColor(img_color,cv2.COLOR_BGR2RGB)))
    #img_show = cv2.cvtColor(np.asarray(img_result),cv2.COLOR_RGB2BGR)
    img_result, alert=ml.detectImage(image,'person')
    if alert:
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img_result,'Alert!!!',(10,80), font, 3,(0,0,255),2,cv2.LINE_AA)
    cv2.imshow('window', img_result) # 如果按下键盘上的 Q 就关闭窗口
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break;
cap.release()
cv2.destroyAllWindows()
