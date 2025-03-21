import numpy as np, cv2

def calc_histo(image, hsize, ranges=[0, 256]):  # 행렬 원소의 1차원 히스토그램 계산
    hist = np.zeros((hsize, 1), np.float32)  #1차원 행렬 생성
    gap = ranges[1] / hsize  # 계급 간격

    #반복문을 이용해서 hist 완성
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            hist[image[i][j] // 16] += 1

    #혹은...
    #for row in image:
    #    for pix in row:
    #        idx = int(pix/gap)
    #        hist[idx] += 1

    #오픈CV함수로도 가능

    return hist

image = cv2.imread("image/pixel.jpg", cv2.IMREAD_GRAYSCALE)  # 영상 읽기
if image is None: raise Exception("영상 파일 읽기 오류 발생")

hsize, ranges = [16], [0, 256]  # 히스토그램 간격수, 값 범위
hist = calc_histo(image, hsize[0], ranges)  # 사용자 정의 히스토그램 계산

print("사용자 정의 함수: \n", hist.flatten())  # 행렬을 벡터로 변환하여 출력
cv2.imshow("image", image)
cv2.waitKey(0)