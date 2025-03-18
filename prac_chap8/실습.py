import numpy as np, cv2

image = cv2.imread("images/scaling.jpg", cv2.IMREAD_GRAYSCALE)

# 역방향 사상으로 최근접 이웃 보간
dst1 = np.zeros((image.shape[0]*2, image.shape[1]*2), np.uint8)
dst2 = np.zeros((image.shape[0]*3, image.shape[1]*3), np.uint8)
# 2배, 3배 크기의 dst 생성

for i in range(dst1.shape[1]):
    for j in range(dst1.shape[0]):
        dst1[j, i] = image[int(j/2), int(i/2)]
# 역방향으로 dst의 j, i 좌표에 들어갈 값을 찾음

for i in range(dst2.shape[1]-1):
    for j in range(dst2.shape[0]-1):
        dst2[j, i] = image[round(j/3), round(i/3)]
# 역방향으로 dst의 j, i에 들어갈 값을 찾음
# 반올림해야함. round 써도 되는데 +0.5해도 같은 의미

#bilinear(양선형 보간법)
dst3 = np.zeros((image.shape[0]*2, image.shape[1]*2), np.uint8)
dst4 = np.zeros((image.shape[0]*3, image.shape[1]*3), np.uint8)

for i in range(dst3.shape[1]):
    for j in range(dst3.shape[0]):
        pt = (i/2, j/2)
        x, y = np.int32(pt)
        if x >= image.shape[1]-1: x = x-1
        if y >= image.shape[0]-1: y = y-1
        P1, P2, P3, P4 = np.float32(image[y:y+2, x:x+2].flatten())
        alpha, beta = pt[1] - y, pt[0] - x
        M1 = P1 + alpha * (P3 - P1)
        M2 = P2 + alpha * (P4 - P2)
        P = M1 + beta * (M2 - M1)
        dst3[j, i] = np.clip(P,0,255)

for i in range(dst4.shape[1]-1):
    for j in range(dst4.shape[0]-1):
        pt = (i/3, j/3)
        x, y = np.int32(pt)
        if x >= image.shape[1]-1 : x = x-1
        if y >= image.shape[0]-1 : y = y-1
        P1, P2, P3, P4 = np.float32(image[y:y+2, x:x+2].flatten())
        alpha, beta = pt[1] - y, pt[0] - x
        M1 = P1 + alpha * (P3 - P1)
        M2 = P2 + alpha * (P4 - P2)
        P = M1 + beta * (M2 - M1)
        dst4[j, i] = np.clip(P,0,255)

cv2.imshow("image", image)
cv2.imshow("image_2NN", dst1)
cv2.imshow("image_3NN", dst2)
cv2.imshow("image_2BI", dst3)
cv2.imshow("image_3BI", dst4)


cv2.waitKey(0)

