import numpy as np, cv2


def draw_histo(hist, shape=(200, 256)):
    hist_img = np.full(shape, 255, np.uint8)
    cv2.normalize(hist, hist, 0, shape[0], cv2.NORM_MINMAX)
    #히스토그램의 값의 최소값과 최대값을 0~200으로 맞춤
    gap = hist_img.shape[1] / hist.shape[0]  # 한 계급 너비

    print(hist)

    for i, h in enumerate(hist):
        x = int(round(i * gap))
        y = int(round(gap))
        cv2.rectangle(hist_img, (x, 0, y, int(h)),0, cv2.FILLED)

    # 영상 상하 뒤집기 후 반환 return
    return np.flip(hist_img, 0)