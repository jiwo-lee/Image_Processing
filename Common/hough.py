import numpy as np, cv2, math

def accumulate(image, rho, theta):
    h, w = image.shape[:2]
    rows, cols = (h+w) * 2 // rho, int(np.pi / theta)
    accumulate = np.zeros((rows, cols), np.int32)

    sin_cos = [(np.sin(t*theta), np.cos(t*theta)) for t in range (cols)]
    pts = np.where(image>0)

    polars = np.dot(sin_cos, pts).T
    polars = (polars / rho + rows / 2).astype('int')

    for row in polars:
        for t, r in enumerate(row):
            accumulate[r, t] += 1
    return accumulate

def masking(accumulate, h, w, thresh):
    rows, cols = accumulate.shape[:2]
    rcenter, tcenter = h//2, w//2
    dst = np.zeros(accumulate.shape, np.uint32)

    for y in range(0, rows, h):
        for x in range(0, cols, w):
            roi = accumulate[y:y+h, x:x+w]
            _, max, _, (x0, y0) = cv2.minMaxLoc(roi)
            dst[y+y0, x+x0] = max
    return dst

def select_lines(acc_dst, rho, theta, thresh):
    rows = acc_dst.shape[0]
    r, t = np.where(acc_dst>thresh)

    rhos = ((r - (rows/2)) * rho)
    radians = t * theta
    values = acc_dst[r, t]

    idx = np.argsort(values)[::-1]
    lines = np.transpose([rhos, radians])
    lines = lines[idx, :]

    return np.expand_dims(lines, axis=1)

def houghLines(src, rho, theta, thresh):
    acc_mat = accumulate(src, rho, theta)  # 허프 누적 행렬 계산
    acc_dst = masking(acc_mat, 7, 3, thresh)  # 마스킹 처리 7행,3열
    lines = select_lines(acc_dst, rho, theta, thresh)  # 직선 가져오기
    return lines

def draw_houghLines(src, lines, nline):
    dst = cv2.cvtColor(src, cv2.COLOR_GRAY2BGR)  # 컬러 영상 변환
    min_length = min(len(lines), nline)

    for i in range(min_length):
        rho, radian = lines[i, 0, 0:2]  # 수직거리 , 각도 - 3차원 행렬임
        a, b = math.cos(radian), math.sin(radian)
        pt = (a * rho, b * rho)  # 검출 직선상의 한 좌표 계산
        delta = (-1000 * b, 1000 * a)  # 직선상의 이동 위치
        pt1 = np.add(pt, delta).astype('int')
        pt2 = np.subtract(pt, delta).astype('int')
        cv2.line(dst, tuple(pt1), tuple(pt2), (0, 255, 0), 2, cv2.LINE_AA)

    return dst