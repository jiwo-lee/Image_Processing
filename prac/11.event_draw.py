import numpy as np
import cv2

def onMouse(event, x, y, flags, param):
    global title, pt

    if event == cv2.EVENT_LBUTTONDOWN:
        if pt[0] < 0 : pt = (x, y) #좌표 변수의 값이 0보다 작으면 클릭한 좌표 넣기
        else:
            cv2.rectangle(image, pt, (x, y), (255,0,0), 2)
            cv2.imshow(title, image)
            pt = (-1, -1)
            #아니면 pt와 클릭한 좌표를 이용해 네모 그리고 pt를 -1 -1로 초기화

    elif event == cv2.EVENT_RBUTTONDOWN:
        if pt[0] < 0 : pt = (x, y)
        else:
            dx, dy = pt[0] - x, pt[1] - y
            radius = int(np.sqrt(dx*dx + dy*dy)) #원의 반지름 구하기
            cv2.circle(image, pt, radius, (0,0,255), 2)
            cv2.imshow(title, image)
            pt = (-1, -1)
            #원 그리고 초기화
#그런데 이건 첫번째 클릭을 뭐로 하든 두번째 클릭에 따라 그려지는 그림이 달라지게 된다

image = np.full((300,500,3), (255,255,255), np.uint8)

pt = (-1, -1) #좌표로 쓸 변수를 -1 -1로 선언
title = "Draw Event"
cv2.imshow(title, image)
cv2.setMouseCallback(title, onMouse)
cv2.waitKey(0)
cv2.destroyAllWindows()