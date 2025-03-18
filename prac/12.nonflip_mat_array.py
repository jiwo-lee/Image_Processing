import cv2
import numpy as np

image = cv2.imread("images/flip_test.jpg", cv2.IMREAD_COLOR)
if image is None: raise Exception("영상 파일 읽기 오류 발생") # 예외 처리
print(image.shape[0]) #267
print(image.shape[1]) #360

image_copy= np.full(image.shape,(255,255,255), np.uint8)
image_flipx = np.full(image.shape,(255,255,255), np.uint8)
image_flipy = np.full(image.shape,(255,255,255), np.uint8)
image_flipxy = np.full(image.shape,(255,255,255), np.uint8)
image_trans = np.full((image.shape[1], image.shape[0],image.shape[2]),(255,255,255), np.uint8)
image_rep = np.full((image.shape[0], image.shape[1]*2,image.shape[2]),(255,255,255), np.uint8)


for i in range(image.shape[0]):
    for j in range(image.shape[1]):
        image_copy[i][j] = image[i][j]
        image_flipx[image.shape[0]-1-i][j] = image[i][j]
        image_flipy[i][image.shape[1]-1-j] = image[i][j]
        image_flipxy[image.shape[0]-1-i][image.shape[1]-1-j] = image[i][j]
        image_trans[j][i] = image[i][j]
        image_rep[i][j] = image[i][j]
        image_rep[i][j+image.shape[1]] = image[i][j]



## 각 행렬을 영상으로 표시
titles = ['image', 'x_axis', 'y_axis','xy_axis','rep_image','trans_image']
titles_copy = ['image_copy', 'image_flipx', 'image_flipy', 'image_flipxy', 'image_trans', 'image_rep']

for title in titles_copy:
    cv2.imshow(title, eval(title))

cv2.waitKey(0)