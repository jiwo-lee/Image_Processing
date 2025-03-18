import numpy as np, cv2

def onchange1(value):
    global im1_trackbar
    im1_trackbar = cv2.getTrackbarPos('image1', title) / 100

def onchange2(value):
    global im2_trackbar
    im2_trackbar = cv2.getTrackbarPos('image2', title) / 100

# 트랙바 슬라이더가 바뀔때마다 trackbar 변수에 슬라이더 위치 / 100 한 값을 줌

image1 = cv2.imread("images/add1.jpg", cv2.IMREAD_GRAYSCALE)
if image1 is None: raise Exception("영상 파일 읽기 오류")

image2 = cv2.imread("images/add2.jpg", cv2.IMREAD_GRAYSCALE)
if image2 is None: raise Exception("영상 파일 읽기 오류")

dst = np.zeros((image1.shape[0], image1.shape[1]*3), np.uint8)
dst[:,:image1.shape[0]] = image1
dst[:,image2.shape[0]*2:] = image2
# dst 선언 및 image1과 image2를 양 옆에 넣음

title = 'dst'
im1_trackbar = 0
im2_trackbar = 0

cv2.imshow(title, dst)
cv2.createTrackbar('image1', title, 40, 100, onchange1)
cv2.createTrackbar('image2', title, 27, 100, onchange2)
# 트랙바를 만들고 onchange1, 2가 작동하게 만듬

while True:
    blendingimage = cv2.addWeighted(image1, im1_trackbar, image2, im2_trackbar, 0)
    dst[:, image2.shape[1]:image2.shape[1] * 2] = blendingimage[:]
    # 블렌딩하고 dst에 이미지 대입

    cv2.imshow(title, dst)
    # 화면 띄움

    k = cv2.waitKey(1) # 1ms 동안 키 입력을 대기 받는다
    # 이렇게 안하고 0으로 하면 트랙바 바꾸고 아무 키 눌러야 트랙바 슬라이드 위치가 반영됨
    # waitkey를 안하면 무한 반복...
    if k == 27: # esc 누르면 탈출
        break

cv2.destroyAllWindows() # 모든 창 닫기