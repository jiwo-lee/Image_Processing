import numpy as np, cv2
def scaling(img, size):  # 크기 변경 함수
    dst = np.zeros(size[::-1], img.dtype)  # size와 shape는 원소가 역순
    ratioY, ratioX = np.divide(size[::-1], img.shape[:2]) # 비율 계산
    y = np.arange(0, img.shape[0], 1) # 입력 영상 세로 좌표 생성
    x = np.arange(0, img.shape[1], 1) # 입력 영상 가로 좌표 생성
    y, x = np.meshgrid(y, x) # x y 크기의 좌표행렬 생성
    i, j = np.int32(y * ratioY), np.int32(x * ratioX) # 목적 영상 좌표 계산
    dst[i, j] = img[y, x] # 목적 영상 좌표에 입력 영상의 해당 좌표 넣음
    return dst

def scaling_nearest(img, size):                                # 크기 변경 함수
    dst = np.zeros(size[::-1], img.dtype)               # 행렬과 크기는 원소가 역순
    ratioY, ratioX = np.divide(size[::-1], img.shape[:2])
    i = np.arange(0, size[1], 1)
    j = np.arange(0, size[0], 1)
    i, j = np.meshgrid(i, j)
    y, x = np.int32(i / ratioY), np.int32(j / ratioX)
    dst[i,j] = img[y,x]

    return dst