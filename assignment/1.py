import numpy as np, cv2

image = np.full((200,300,3), (255, 255, 255), np.uint8)

center = (image.shape[1]//2, image.shape[0]//2) # 태극문양의 중점
pt1 = (image.shape[1]//2 - 25, image.shape[0]//2) # 태극문양 물결 그릴 때 쓰일 좌표1
pt2 = (image.shape[1]//2 + 25, image.shape[0]//2) # 태극문양 물결 그릴 때 쓰일 좌표2
size1 = (50, 50) # 원의 위아래/좌우 사이즈
size2 = (25, 25) # 태극 문양 물결 그릴때 쓰일 사이즈
red = (0, 0, 255)
blue = (255, 0, 0)

cv2.ellipse(image, center, size1, 180, 0, 180, red, -1) # 태극문양 빨간 반원
cv2.ellipse(image, center, size1, 0, 0, 180, blue, -1) # 태극문양 파란 반원
cv2.ellipse(image, pt1, size2, 0, 0, 180, red, -1) # 태극문양 빨간 물결
cv2.ellipse(image, pt2, size2, 180, 0, 180, blue, -1) #태극문양 파란 물결

cv2.imshow("py1", image)
cv2.waitKey(0)