import numpy as np
import cv2

image = np.zeros((200,300), np.uint8)
image.fill(255) # 가로300 세로200 크기에 색상 255인 이미지를 행렬로 생성

title1, title2 = 'Autosize', 'Normal'
cv2.namedWindow(title1, cv2.WINDOW_AUTOSIZE)
cv2.namedWindow(title2, cv2.WINDOW_NORMAL)

cv2.imshow(title1, image)
cv2.imshow(title2, image) #윈도우 창을 보여준다
cv2.resizeWindow(title1, 400, 300) #창 크기 변경 함수, 가로 400, 세로 300으로 바뀐다
cv2.resizeWindow(title2, 400, 300)
#AUTOSIZE였던 것은 이미지의 크기는 가로 300 세로 200으로 남고 윈도우 창만 늘어난다
#그러나 NORMAL은 윈도우 창의 크기만큼 이미지의 크기도 늘어났다. 그러나 실제 행렬은 변하지 않는다.
cv2.waitKey(0) #키 입력 될때까지 대기
cv2.destroyAllWindows() #모든 창을 닫음
