import os
import cv2
from PIL import Image
# 打开视频文件
cap = cv2.VideoCapture('video path')
frame_count = 0  # 帧计数器

# 逐帧读取和处理视频
while cap.isOpened():
    # 读取一帧
    ret, frame = cap.read()
    if not ret:
        break
    if frame_count % 5 == 0: 
        Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)).save(f'image path/frame{frame_count}.jpg')
        print(f"Saved frame{frame_count}.jpg")
    frame_count += 1 
# 释放资源
cap.release()
