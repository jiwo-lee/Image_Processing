import cv2

image = cv2.imread("image/pixel.jpg", cv2.IMREAD_GRAYSCALE) # 영상 읽기
if image is None: raise Exception("영상 파일 읽기 오류")

(x,y),(w,h) = (180, 37), (15, 10)                   # 좌표는 x, y
roi_img = image[y:y+h, x:x+w]                   # 행렬 접근은 y, x
#이미지에서 원하는 영역만 선택

#print(“[roi_img] =\n”, roi_img) # 행렬 원소 바로 출력 가능

print("[roi_img] =")
for row in roi_img:
    for p in row:
        print("%4d" % p, end="")       # 행렬 원 하나 출력
    print()
#선택한 영역의 원소값 출력

cv2.rectangle(image, (x,y, w,h), 255, 1)
#선택한 영역을 이미지상에 표시하기 위해 사각형을 그림
cv2.imshow("image", image)
cv2.waitKey(0)