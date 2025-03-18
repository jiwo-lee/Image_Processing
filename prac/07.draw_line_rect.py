import numpy as np
import cv2

blue, green, red = (255,0,0), (0,255,0), (0,0,255)
image = np.zeros((400,600,3), np.uint8)
image[:] = (255,255,255)

pt1, pt2 = (50,50), (250,150)
pt3, pt4 = (400,150), (500,50)
roi = (50,200,200,100)

#선그리기
cv2.line(image, pt1, pt2, red)
cv2.line(image, pt3, pt4, green, 3, cv2.LINE_AA) #LINE_AA는 안티엘리어싱

#사각형그리기
cv2.rectangle(image, pt1, pt2, blue, 3, cv2.LINE_4)
#pt1과 pt2가 대각선상에 위치한 꼭지점인 굵기 3의 파란색 4방향 연결선의 테두리 가진 사각형
cv2.rectangle(image, roi, red, 3, cv2.LINE_8)
#roi(시작점이 50, 200이고 가로 200 세로 100)인 굴기 3의 빨간색 8방향 연결선의 테두리 가진 사각형
cv2.rectangle(image, (400,200,100,100), green, cv2.FILLED)
#cv2.FILLED는 내부를 테두리와 같은 색으로 채운다

cv2.imshow("Line & Rectangle", image)
cv2.waitKey(0)
cv2.destroyAllWindows()