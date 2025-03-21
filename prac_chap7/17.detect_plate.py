import numpy as np, cv2

while True:
    no = int(input("차량 영상 번호( 0:종료 ) : "))             # 차량 번호 입력받아서 no에 저장
    if no == 0: break; # no에 저장된 값이 0이면 반복문 탈출

    fname = "images/test_car/{0:02d}.jpg".format(no) # 불러올 사진의 이름 구성
    image = cv2.imread(fname, cv2.IMREAD_COLOR)
    if image is None:
        print(str(no) + "번 영상 파일이 없습니다.")
        continue

    mask = np.ones((5,17), np.uint8)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.blur(gray, (5, 5))
    gray = cv2.Sobel(gray, cv2.CV_8U, 1, 0, 5)

    th_img = cv2.threshold(gray, 120, 255, cv2.THRESH_BINARY)[1]
    morph = cv2.morphologyEx(th_img, cv2.MORPH_CLOSE, mask, iterations=3)

    cv2.imshow("image", image)
    cv2.imshow("binary image", th_img)
    cv2.imshow("opening", morph)
    cv2.waitKey()
