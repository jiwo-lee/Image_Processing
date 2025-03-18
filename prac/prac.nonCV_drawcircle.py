import numpy as np
import cv2

orange, blue, cyan = (0, 160, 255), (255, 0, 0), (255, 255, 0)
white, black = (255,255,255), (0,0,0)
image = np.full((300,500,3), white, np.uint8)

center = (image.shape[1]//2, image.shape[0]//2)
#원의 중점의 좌표 저장

for i in range(center[0]-100, center[0]+101, 1):
    j1 = center[1] + np.sqrt(10000 - (i - center[0])**2)
    j2 = center[1] - np.sqrt(10000 - (i - center[0])**2)
    image[int(j1)][i][0] = 0
    image[int(j1)][i][1] = 0
    image[int(j1)][i][2] = 0
    image[int(j2)][i][0] = 0
    image[int(j2)][i][1] = 0
    image[int(j2)][i][2] = 0
#x축을 기준으로 그림을 그린다.
#원에서 y좌표는 (중점y) +- np.sqrt(반지름제곱 - (x좌표 - 중점x)제곱)이다
#그런데 이 함수는 x축당 하나의 y좌표만 찾아서 점을 찍기 때문에 for문만 갖고는 양 끝이 희미하게 보인다

for i in range(center[1]-100, center[1]+101, 1):
    j1 = center[0] + np.sqrt(10000 - (i - center[1])**2)
    j2 = center[0] - np.sqrt(10000 - (i - center[1])**2)
    image[i][int(j1)][0] = 0
    image[i][int(j1)][1] = 0
    image[i][int(j1)][2] = 0
    image[i][int(j2)][0] = 0
    image[i][int(j2)][1] = 0
    image[i][int(j2)][2] = 0
#따라서 y축 기준으로 그림을 한번 더 그려서 원을 제대로 그려줌

title = "Draw Circle"
cv2.namedWindow(title)
cv2.imshow(title, image)
cv2.waitKey(0)