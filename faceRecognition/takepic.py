import cv2
import os

def take(name,folder):
    cap = cv2.VideoCapture(0)
    #cap = cv2.VideoCapture('/Users/i037762/Desktop/ch08_20180919234933.mp4')
    i=0
    while(True): # 从摄像头中读取画面，while表示循环读取画面，也就是一张一张图片形成了一个视频
        ret, image = cap.read()
        cv2.imshow("Camera", image)
        q=cv2.waitKey()
        if q & 0xFF == ord('s'):
            cv2.imwrite(folder+os.sep+name+'%s%d.jpg'%(name,i), image)
            i=i+1
            continue
        elif q & 0xFF == ord('n'):
            continue
        elif q & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
if __name__ == '__main__':
    take('lizzie','./dataset/lizzie')
