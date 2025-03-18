import numpy as np, cv2

image = cv2.imread("images/bit_test.jpg", cv2.IMREAD_COLOR)     # 원본 영상 읽기
logo  = cv2.imread("images/logo.jpg", cv2.IMREAD_COLOR)         # 로고 영상 읽기
if image is None or logo is None: raise Exception("영상 파일 읽기 오류 ")

masks = cv2.threshold(logo, 220, 255, cv2.THRESH_BINARY)[1]  # 로고 영상 이진화
#logo에서 220 이상 값들은 255로 만들고 나머지는 0으로 이진화
masks = cv2.split(masks) #3채널을 각각 분리한다

fg_pass_mask = cv2.bitwise_or(masks[0], masks[1])       # 전경 통과 마스크
fg_pass_mask = cv2.bitwise_or(masks[2], fg_pass_mask)   # 하나라도 흰색(1)이면 1이 된다
bg_pass_mask = cv2.bitwise_not(fg_pass_mask)            # 배경 통과 마스크 전경통과마스크의 부정.

(H, W), (h, w) = image.shape[:2], logo.shape[:2]                       # 로고 영상 크기
x, y = (W-w)//2, (H - h)//2     #image에서 logo의 크기만큼만 잘라낼거기 때문에 logo의 왼쪽 위 좌표를 구함
roi = image[y:y+h, x:x+w]                # 관심 영역(roi) 지정
#logo의 왼쪽 위 좌표에 logo의 크기만큼을 더하면 오른쪽 아래 좌표가 나오니 logo의 위치만큼 image를 잘라냄

# 행렬 논리곱과 마스킹을 이용한 관심 영역 복사
foreground = cv2.bitwise_and(logo, logo, mask=fg_pass_mask) # 로고의 전경 복사
#로고와 전경 통과 마스크를 곱해서 배경을 투명화(로고에서 로고 배경이 검음)
background = cv2.bitwise_and(roi , roi , mask=bg_pass_mask) # roi에 원본배경만 복사
#관심영역과 배경 통과 마스크를 곱해서 로고를 투명화(배경 이미지(관심 영역)에 로고 부분을 합성해 로고 부분 검음)

dst = cv2.add(background, foreground)            # 로고 전경과 원본 배경 간 합성
#배경이 투명한(정확힌 값이 0인) 로고와 로고부분이 투명한(값이 0인) 배경이미지를 합함
image[y:y+h, x:x+w] = dst             # 합성 영상을 원본에 복사

cv2.imshow("background", background);  cv2.imshow("forground", foreground)
cv2.imshow("dst", dst);                 cv2.imshow("image", image)
cv2.waitKey()