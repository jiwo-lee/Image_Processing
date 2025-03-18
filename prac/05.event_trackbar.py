import numpy as np
import cv2

def onchage(value):
    global image, title

    add_value = value - int(image[0][0]) #value(트랙바의 위치)와 기존 이미지의 밝기 값
    print("추가 화소값:", add_value) #바뀐 밝기만큼 출력
    image[:] = image + add_value #이미지 행렬 전부 값을 바꿈
    cv2.imshow(title, image) #바뀐 이미지를 보여줌
#함수 선언

image = np.zeros((300,500), np.uint8) #색 지정 안해서 검정색

title = "Trackbar Event"
cv2.imshow(title, image)

cv2.createTrackbar('Brightness', title, image[0][0], 255, onchage)
#Brightness라는 이름을 가진 트랙바를 title 제목을 가진 윈도우에 넣음
#시작값은 image의 0,0에 있는 값, 최대값은 255, 슬라이더 값이 바뀔때 onchange함수 작동
cv2.waitKey(0)
cv2.destroyAllWindows()