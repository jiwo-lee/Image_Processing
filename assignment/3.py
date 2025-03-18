import numpy as np, cv2

image = cv2.imread("images/color.jpg", cv2.IMREAD_COLOR)
if image is None: raise Exception("영상 파일 읽기 오류")
if image.ndim != 3: raise Exception("컬러 영상 아님")

bgr = cv2.split(image) # 이미지 채널 분리

red = np.zeros(image.shape, np.uint8)
blue = np.zeros(image.shape, np.uint8)
green = np.zeros(image.shape, np.uint8)
# image와 똑같은 크기의 3차원 행렬 생성

red[:,:,2] = bgr[2]
green[:,:,1] = bgr[1]
blue[:,:,0] = bgr[0]
# 각 색상에 맞는 위치에 넣기

cv2.imshow("Blue channel", blue)
cv2.imshow("Green channel", green)
cv2.imshow("Red channel", red)
cv2.waitKey(0)