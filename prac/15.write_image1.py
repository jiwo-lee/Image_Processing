import cv2

image = cv2.imread("images/read_color.jpg", cv2.IMREAD_COLOR)
if image is None: raise Exception("영상 파일 읽기 에러")
    
params_jpg = (cv2.IMWRITE_JPEG_QUALITY, 80)        # JPEG 화질 설정
#숫자가 작다 -> 압축이 잘되지만 그만큼 이미지 손상도 크다
params_png = [cv2.IMWRITE_PNG_COMPRESSION, 0]       # PNG 압축 레벨 설정
#숫자가 크다 -> 압축이 잘되지만 그만큼 시간이 걸린다(이미지 손상은 적음)

## 행렬을 영상 파일로 저장
cv2.imwrite("images/write_test1.jpg", image)       # 디폴트는 95
cv2.imwrite("images/write_test2.jpg", image, params_jpg) # 지정 화질로 저장
cv2.imwrite("images/write_test3.png", image, params_png)
cv2.imwrite("images/write_test4.bmp", image)         # BMP 파일로 저장
print("저장 완료")