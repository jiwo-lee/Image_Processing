import numpy as np, cv2

image1 = np.zeros((300, 300), np.uint8)     		# 300행, 300열 검은색 영상 생성
image2 = image1.copy()

h, w = image1.shape[:2]
cx,cy  = w//2, h//2
cv2.circle(image1, (cx,cy), 100, 255, -1)      # 이미지 중심에 하얀 원 그리기
cv2.rectangle(image2, (0,0, cx, h), 255, -1)    #이미지 좌측 절반을 하얀색으로

image3 = cv2.bitwise_or(image1, image2)     	# 원소 간 논리합
image4 = cv2.bitwise_and(image1, image2)    	# 원소 간 논리곱
image5 = cv2.bitwise_xor(image1, image2)    	# 원소 간 배타적 논리합
image6 = cv2.bitwise_not(image1)            	# 행렬 반전

cv2.imshow("image1", image1);			cv2.imshow("image2", image2)
cv2.imshow("bitwise_or", image3);		cv2.imshow("bitwise_and", image4)
cv2.imshow("bitwise_xor", image5);	cv2.imshow("bitwise_not", image6)
cv2.waitKey(0)