import numpy as np
import cv2

image = np.zeros((200,400), np.uint8)
image[:] = 200 # 가로400 세로200 크기에 색상 200인 이미지를 행렬로 생성

title1, title2 = 'position1', 'position2'
cv2.namedWindow(title1, cv2.WINDOW_AUTOSIZE)
cv2.namedWindow(title2) #title1, 2 변수에 저장된 글자를 제목으로 하는 윈도우 생성, 윈도우 크기는 변경 X
cv2.moveWindow(title1, 150, 150)
cv2.moveWindow(title2, 400, 50)
#윈도우창이 지정된 위치로 이동

cv2.imshow(title1, image)
cv2.imshow(title2, image) #윈도우 창을 보여준다
cv2.waitKey(0) #키 입력 될때까지 대기
cv2.destroyAllWindows() #모든 창을 닫음

