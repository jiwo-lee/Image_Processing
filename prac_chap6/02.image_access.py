import numpy as np, cv2, time

#이미지의 각 화소에 접근해 화소의 값을 건드려 흑백을 반전시키는 방법들
def pixel_access1(image):
    image1 = np.zeros(image.shape[:2], image.dtype)
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            pixel = image[i,j]                  # 화소 접근
            image1[i, j] =  255 - pixel            # 화소 할당
    return image1
#직접 접근 방법
#시간이 가장 오래 걸림

def pixel_access2(image):
    image2 = np.zeros(image.shape[:2], image.dtype)
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            pixel = image.item(i, j)  # 화소 접근
            image2.itemset((i, j),  255 - pixel)  # 화소 할당
    return image2
#item함수를 이용한 접근 방법
#직접 접근 방법 다음으로 시간이 오래걸림

def pixel_access3(image):
    lut = [255 - i for i in range(256)]  # 룩업테이블 생성
    print(lut)
    lut = np.array(lut, np.uint8)
    image3 = lut[image]
    return image3
#룩업테이블을 이용한 접근 방법
#룩업테이블은 만들때의 시간이 걸린다.

def pixel_access4(image):
    image4 = cv2.subtract(255, image)
    return image4
#cv2 함수를 이용한 접근 방법

def pixel_access5(image):
    image5 = 255 - image
    return image5
#ndarray 산술 연산 방법
#가장 빠른 방법

image = cv2.imread("image/bright.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상 파일 읽기 오류 발생")

# 수행시간 체크
def time_check(func, msg):
    start_time = time.perf_counter()
    ret_img = func(image)
    elapsed = (time.perf_counter() - start_time) * 1000
    print(msg, "수행시간 : %.2f ms" % elapsed)
    return ret_img

image1 = time_check(pixel_access1, "[방법 1] 직접 접근 방식")
image2 = time_check(pixel_access2, "[방법 2] item() 함수 방식")
image3 = time_check(pixel_access3, "[방법 3] 룩업 테이블 방식")
image4 = time_check(pixel_access4, "[방법 4] OpenCV 함수 방식")
image5 = time_check(pixel_access5, "[방법 5] ndarray 연산 방식")

# 결과 영상 보기
cv2.imshow("image  - original", image)
cv2.imshow("image1 - directly access to pixel", image1)
cv2.imshow("image2 - item()/itemset()", image2)
cv2.imshow("image3 - LUT", image3)
cv2.imshow("image4 - OpenCV", image4)
cv2.imshow("image5 - ndarray 방식", image5)
cv2.waitKey(0)