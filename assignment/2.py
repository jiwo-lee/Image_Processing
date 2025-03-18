import numpy as np, cv2

def search_value_idx(hist, bias = 0): # 값이 존재하는 첫 계급을 찾기
    for i in range(hist.shape[0]):
        idx = np.abs(bias - i) # bias - i의 절대값 처음 또는 마지막부터
        if hist[idx] > 0: return idx # idx 위치의 hist가 0이 아니라면 idx 반환
    return -1

def onMouse(event, x, y, flags, param):  # 클릭 이벤트
    global pt
    if event == cv2.EVENT_LBUTTONDOWN:
        pt = (x, y)  # 클릭한 구간의 좌표

        bsize, ranges = [32], [0, 256]  # 계급의 수, 화소 범위
        if pt[1] - 50 < 0 :
            roi = image[0:pt[1] + 51, pt[0] - 50:pt[0] + 51]
        elif pt[1] + 51 > image.shape[0] :
            roi = image[pt[1] - 50:image.shape[0], pt[0] - 50:pt[0] + 51]
        elif pt[0] - 50 < 0 :
            roi = image[pt[1] - 50:pt[1] + 51, 0:pt[0] + 51]
        elif pt[0] + 51 > image.shape[1]:
            roi = image[pt[1] - 50:pt[1] + 51, pt[0] - 50:image.shape[1]]
        else : roi = image[pt[1] - 50:pt[1] + 51, pt[0] - 50:pt[0] + 51]
        # -50~+50 범위가 이미지 크기 벗어나는 경우를 예외 처리
        hist = cv2.calcHist([roi], [0], None, bsize, ranges)  # 관심영역 히스토그램 계산

        bin_width = ranges[1] / bsize[0]  # 한 계급의 너비 256/256 = 1
        high = search_value_idx(hist, bsize[0] - 1) * bin_width  # 최고 화소값
        low = search_value_idx(hist, 0) * bin_width  # 최저 화소값

        idx = np.arange(0, 256) # 0~256
        idx = (idx - low) / (high - low) * 255 # 각 화소값에 계산해 stretch
        idx[0:int(low)] = 0
        idx[int(high + 1):] = 255 #히스토그램 하위와 상위를 0과 255로 지정

        dst = idx.astype('uint8')[roi]
        if pt[1] - 50 < 0:
            image[0:pt[1] + 51, pt[0] - 50:pt[0] + 51] = dst
        elif pt[1] + 51 > image.shape[0]:
            image[pt[1] - 50:image.shape[0], pt[0] - 50:pt[0] + 51] = dst
        elif pt[0] - 50 < 0:
            image[pt[1] - 50:pt[1] + 51, 0:pt[0] + 51] = dst
        elif pt[0] + 51 > image.shape[1]:
            image[pt[1] - 50:pt[1] + 51, pt[0] - 50:image.shape[1]] = dst
        else:
            image[pt[1] - 50:pt[1] + 51, pt[0] - 50:pt[0] + 51] = dst
        # -50~+50 범위가 이미지 크기 벗어나는 경우를 예외 처리
        cv2.imshow("image", image)


image = cv2.imread("images/equalize.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상 파일 읽기 오류")

pt = (0, 0)

cv2.imshow("image", image)
cv2.setMouseCallback("image", onMouse)
cv2.waitKey(0)