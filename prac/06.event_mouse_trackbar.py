import numpy as np
import cv2

def onChange(value):
    global image, title

    add_value = value - int(image[0][0])  # value(트랙바의 위치)와 기존 이미지의 밝기 값
    image[:] = image + add_value  # 이미지 행렬 전부 값을 바꿈
    cv2.imshow(title, image)  # 바뀐 이미지를 보여줌
# 함수 선언

def onMouse(event, x, y, flags, param):
    global image, bar_name

    if event == cv2.EVENT_RBUTTONDOWN:
        if (image[0][0] < 246): image[:] = image + 10
        cv2.setTrackbarPos(bar_name, title, image[0][0])
        cv2.imshow(title, image)

    elif event == cv2.EVENT_LBUTTONDOWN:
        if (image[0][0] >= 10): image[:] = image - 10
        cv2.setTrackbarPos(bar_name, title, image[0][0])
        cv2.imshow(title, image)

image = np.zeros((300,500), np.uint8)
title = "Trackbar & Mouse Event"
bar_name = 'Brightness'
cv2.imshow(title, image)

cv2.createTrackbar(bar_name, title, image[0][0], 255, onChange)
cv2.setMouseCallback(title, onMouse)
cv2.waitKey(0)
cv2.destroyAllWindows()