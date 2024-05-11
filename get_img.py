import cv2
 
capture = cv2.VideoCapture(0)   # 打开笔记本内置摄像头
cv2.VideoCapture.set(capture, 3, 1080)  # 参数3表示设置的是宽的分辨率
cv2.VideoCapture.set(capture, 4, 780)  # 参数4表示设置的是高的分辨率

while capture.isOpened():      # 笔记本摄像头被打开
    retval, image = capture.read()  # 从摄像头中实时读取视频
    if capture.isOpened() :
        cv2.imshow("Video", image)  # 在窗口显示读取到的视频
        cv2.moveWindow('Video', 100, 178)
    key = cv2.waitKey(1)     # 等待用户按下键盘按键的时间为1毫秒
    if key == 32:
        break
capture.release()   # 关闭摄像头
cv2.destroyAllWindows()