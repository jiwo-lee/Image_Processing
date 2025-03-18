import numpy as np, cv2

def dilate(img, mask):
    dst = np.zeros(img.shape, np.uint8)
    if mask is None: mask = np.ones((3, 3), np.uint8)
    ycenter, xcenter = np.divmod(mask.shape[:2], 2)[0]

    for i in range(ycenter, img.shape[0] - ycenter):    # 입력 행렬 반복 순회
        for j in range(xcenter, img.shape[1] - xcenter):
            y1, y2 = i - ycenter, i + ycenter + 1       # 마스크 높이 범위
            x1, x2 = j - xcenter, j + xcenter + 1       # 마스크 너비 범위
            roi = img[y1:y2, x1:x2]                     # 마스크 영역
            temp = cv2.bitwise_and(roi, mask)           # 관심영역과 마스크의 합연산
            cnt  = cv2.countNonZero(temp) # 관심영역과 마스크의 일치한 화소수를 계산해서 cnt에 저장
            dst[i, j] = 0 if (cnt == 0) else 255  # cnt가 0이면 i, j에 0을, 아니면 255를 저장
    return dst

image = cv2.imread("images/morph.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상파일 읽기 오류")

mask = np.array([[0, 1, 0],                         # 마스크 초기화
                 [1, 1, 1],
                 [0, 1, 0]]).astype("uint8")
th_img = cv2.threshold(image, 128, 255, cv2.THRESH_BINARY)[1]  # 영상 이진화
dst1 = dilate(th_img, mask)                              # 사용자 정의 팽창 함수
dst2 = cv2.morphologyEx(th_img, cv2.MORPH_DILATE, mask)  # OpenCV의 팽창 함수
# dst2 = cv2.dilate(th_img, mask)

cv2.imshow("User dilate", dst1)
cv2.imshow("OpenCV dilate", dst2)
cv2.waitKey(0)