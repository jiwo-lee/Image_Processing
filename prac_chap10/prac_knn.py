import numpy as np, cv2

def draw_points(image, group, color):
    for p in group:
        pt = tuple(p.astype(int))
        cv2.circle(image, pt, 3, color, cv2.FILLED)

nsample = 20
traindata = np.zeros((nsample*2, 2), np.float32)  # 학습 데이터 행렬
label = np.zeros((nsample*2, 1), np.float32)   # 레이블


cv2.randn(traindata[:nsample], 50, 30)
cv2.randn(traindata[nsample:], 100, 60)


label[:nsample], label[nsample:] = 0 , 1

K = 1

image = np.zeros((200, 200, 3))
dist = np.zeros(nsample*2)



draw_points(image, traindata[:nsample], color=(0, 0, 255))
draw_points(image, traindata[nsample:], color=(0, 255, 0))

cv2.imshow("sample K="+ str(K), image)
cv2.waitKey(0)