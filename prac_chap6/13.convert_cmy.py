import numpy as np, cv2

BGR_img = cv2.imread("image/color_model.jpg", cv2.IMREAD_COLOR) # 컬러 영상 읽기
if BGR_img is None: raise Exception("영상 파일 읽기 오류")
    
white = np.array([255, 255, 255], np.uint8) #255로 값이 가득찬 array
CMY_img = white - BGR_img #cyan = 255 - Red / magenta = 255 - Green / Yellow = 255 - Blue
Cyan, Magenta, Yellow = cv2.split(CMY_img) # 채널 분리

titles = ['BGR_img','CMY_img','Cyan','Magenta','Yellow']
[cv2.imshow(t, eval(t)) for t in titles]
cv2.waitKey(0)