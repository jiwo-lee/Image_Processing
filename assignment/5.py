import numpy as np, cv2

image = cv2.imread("images/bit_test.jpg", cv2.IMREAD_COLOR)     # 원본 영상 읽기
logo = cv2.imread("images/logo.jpg", cv2.IMREAD_COLOR)         # 로고 영상 읽기
if image is None or logo is None: raise Exception("영상 파일 읽기 오류 ")

a = int(input("가로에 들어갈 개수를 입력하시오."))
b = int(input("세로에 들어갈 개수를 입력하시오."))

logo = cv2.resize(logo, (image.shape[1]//a, image.shape[0]//b))
# 로고의 사이즈를 이미지의 가로/가로 개수 세로/세로 개수로 재조정
# 나누기를 쓰면 소수점까지 내려갈수 있으니 나머지를 버린 몫만 쓰기로 함

masks = cv2.threshold(logo, 220, 255, cv2.THRESH_BINARY)[1]
# logo에서 220 이상 값들은 255 = 1로 만들고 나머지는 0으로 이진화
masks = cv2.split(masks) # 3채널을 각각 분리한다

fg_pass_mask = cv2.bitwise_or(masks[0], masks[1])
fg_pass_mask = cv2.bitwise_or(masks[2], fg_pass_mask)
# 전경 통과 마스크 bgr 중 하나라도 1이면 1의 값을 갖는다
bg_pass_mask = cv2.bitwise_not(fg_pass_mask)
# 배경 통과 마스크, 전경 통과 마스크의 부정

h, w = logo.shape[:2] # 로고의 크기
for i in range(a):
    for j in range(b): # for문으로 하나씩 넣을 것
        x, y = i * logo.shape[1], j * logo.shape[0] # 시작 좌표
        roi = image[y:y+h, x:x+w] # 시작 좌표와 로고의 사이즈로 관심영역 지정

        foreground = cv2.bitwise_and(logo, logo, mask=fg_pass_mask) # 로고의 전경 복사
        background = cv2.bitwise_and(roi, roi, mask=bg_pass_mask) # roi의 배경만 복사

        dst = cv2.add(background, foreground) # 로고 전경과 roi 배경을 합침
        image[y:y+h, x:x+w] = dst # 합친 것을 이미지에 붙여넣기

cv2.imshow("image", image)
cv2.waitKey(0)