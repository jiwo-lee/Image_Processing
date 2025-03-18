import cv2
from Common.utils import print_matInfo
#Common 디렉토리에 만든 utils 코드에서 print_matInfo 함수 불러옴

title1, title2 = "16bit unchanged", "32bit unchanged"  # 윈도우 이름
color2unchanged1 = cv2.imread("images/read_16.tif", cv2.IMREAD_UNCHANGED)
color2unchanged2 = cv2.imread("images/read_32.tif", cv2.IMREAD_UNCHANGED)
#각각 16비트, 32비트 영상을 cv2.IMREAD_UNCHANGED 옵션으로 적재. 각각 uint16, float32형식 행렬 생성
if color2unchanged1 is None or color2unchanged2 is None: #예외 처리
    raise Exception("영상파일 읽기 에러")

print("16/32비트 영상 행렬 좌표 (10, 10) 화소값")
print(title1, "원소 자료형 ",  type(color2unchanged1[10][10][0]))   # 원소 좌료형
print(title1, "화소값(3원소) ", color2unchanged1[10, 10] )           # 행렬 내 한 화소 값 표시
print(title2, "원소 자료형 ",  type(color2unchanged2[10][10][0]))
print(title2, "화소값(3원소) ", color2unchanged2[10, 10] )
print()
#16비트 영상에서는 0~2^16-1로, 32비트에서는 0~1까지 2^32구간으로 나눠서 사용

print_matInfo(title1, color2unchanged1)         # 행렬 정보 출력
print_matInfo(title2, color2unchanged2)
cv2.imshow(title1, color2unchanged1)
cv2.imshow(title2, (color2unchanged2*255).astype("uint8"))
#화면에 띄울때 uint8형식으로 띄움
cv2.waitKey(0)