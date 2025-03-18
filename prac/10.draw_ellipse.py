import numpy as np
import cv2

orange, blue, white = (0, 165, 255), (255, 0, 0), (255, 255, 255) #색깔
image = np.full((300,700, 3), white, np.uint8) #3차원 행렬

pt1, pt2 = (180,150), (550,150) #타원의 중심점으로 쓸 좌표 2개
size = (120,60) #타원의 x축 y축 반지름 길이로 쓸 것

cv2.circle(image, pt1, 1,0,2)
cv2.circle(image, pt2, 1,0,2)
#좌표 두개에 점을 찍어줌

cv2.ellipse(image, pt1, size, 0, 0, 360, blue, 1) #타원 그리기
cv2.ellipse(image, pt2, size, 90, 0, 360, blue, 1) #90도 돌아간 타원
cv2.ellipse(image, pt1, size, 0, 30, 270, orange, 4) #호 그리기
cv2.ellipse(image, pt2, size, 90, 30, 270, orange, 4) #90도 돌아간 호

cv2.imshow("타원", image)
cv2.waitKey(0)
cv2.destroyAllWindows()