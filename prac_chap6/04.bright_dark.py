import cv2

image = cv2.imread("image/bright.jpg", cv2.IMREAD_GRAYSCALE)    # 영상 읽기
if image is None: raise Exception("영상 파일 읽기 오류")

# OpenCV 함수 이용
dst1 = cv2.add(image, 100)                  # 영상에 100을 더함(밝게) saturation 방식
dst2 = cv2.subtract(image, 100)             # 영상에 100을 뺌(어둡게)
#OpenCV 함수는 saturation 방식을 사용 -> 255를 넘어가거나 0보다 작아져도 그냥 255와 0으로 취급

# numpy array 이용
dst3 = image + 100                          # 영상에 100을 더함(밝게) modulo 방식
dst4 = image - 100                          # 영상에 100을 뺌(어둡게)
#numpy는 modulo 방식을 사용 -> 255를 넘어가거나 0보다 작아지면 나누기해서 나머지값을 넣음(오버플로우 일어남)

cv2.imshow("original image", image)
cv2.imshow("dst1- bright: OpenCV", dst1)
cv2.imshow("dst2- dark: OpenCV", dst2)
cv2.imshow("dst3- bright: numpy", dst3)
cv2.imshow("dst4- dark: numpy", dst4);
cv2.waitKey(0)