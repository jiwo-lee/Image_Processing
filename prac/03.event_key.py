import numpy as np
import cv2

#키보드 입력하면 그 입력한것을 출력하는 프로그램

switch_case = {
    ord('a'): "a키 입력", #ord 함수 : 문자 -> 아스키코드 변환
    ord('b'): "b키 입력",
    0x41: "A키 입력",
    int('0x42', 16): "B키 입력", #16진수 0x42를 10진수 변환
    2424832: "왼쪽 화살표키 입력",
    2490368: "위쪽 화살표키 입력",
    2555904: "오른쪽 화살표키 입력",
    2621440: "아래쪽 화살표키 입력"
}

image = np.ones((200,300), np.float32) #원소값이 1인 행렬 생성
cv2.namedWindow('Keyboard event')
cv2.imshow("Keyboard Event", image)

while True:
    key = cv2.waitKeyEx(100)
    if key == 27: break

    try:
        result = switch_case[key]
        print(result)
    except KeyError:
        result = -1

cv2.destroyAllWindows()
