import numpy as np, cv2

def onMouse(event, x, y, flags, param):
    global title, pt

    if event == cv2.EVENT_LBUTTONDOWN:
        if pt[0] < 0 : pt = (x, y) #좌표 변수의 값이 0보다 작으면 클릭한 좌표 넣기
        else:
            roi = image[pt[1]:y, pt[0]:x]
            hist = cv2.calcHist([roi], [0], None, [32], [0,256])
            hist_img = draw_histo(hist)
            cv2.imshow("hist_img", hist_img)
            # 클릭한 부분을 관심영역으로 지정하고 히스토그램 계산 후 히스토그램 그려서 출력

            cv2.rectangle(image, pt, (x, y), (0), 2)
            cv2.imshow(title, image)
            # 사각형을 image 위에 그린다.
            # 이게 히스토그램 계산보다 먼저 실행되면 히스토그램에 검정색 사각형까지 포함되어 계산된다

            pt = (-1, -1) #값 초기화

def draw_histo(hist, shape=(200, 256)):
    hist_img = np.full(shape, 255, np.uint8)
    cv2.normalize(hist, hist, 0, shape[0], cv2.NORM_MINMAX)
    # 히스토그램의 값의 최소값과 최대값을 0~200으로 맞춤
    gap = hist_img.shape[1] / hist.shape[0]  # 한 계급의 너비

    print(hist)

    for i, h in enumerate(hist):
        x = int(round(i * gap))
        w = int(round(gap))
        cv2.rectangle(hist_img, (x, 0, w, int(h)), 0, cv2.FILLED)
    # 히스토그램의 검은색 정사각형 그리기

    # 영상 상하 뒤집기 후 반환 return
    return np.flip(hist_img, 0)

image = cv2.imread("images/pixel.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상 파일 읽기 오류")

title = 'result'
pt = (-1, -1)

cv2.imshow(title, image)
cv2.setMouseCallback(title, onMouse)
cv2.waitKey(0)