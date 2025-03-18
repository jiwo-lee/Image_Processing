import numpy as np
import cv2

# numpy array이용해 단일 채널 3개 생성
ch0 = np.zeros((2, 4), np.uint8) + 10           # 0원소 행렬 선언 후 10 더하기
ch1 = np.ones((2, 4), np.uint8) * 20            # 1원소 행렬 선언 후 20 곱하기
ch2 = np.zeros((2, 4), np.uint8); ch2[:] = 30   # 0원소 행렬 선언 후 행렬원소값 30 지정

list_bgr = [ch0, ch1, ch2]                      # 단일 채널들을 모아 리스트 구성 [10, 20, 30]으로 들어감
merge_bgr = cv2.merge(list_bgr)                 # 채널 합성해서 merge_bgr로 선언
split_bgr = cv2.split(merge_bgr)                # 채널 분리: 컬러영상(merge_bgr)--> 3채널 분리
#merge의 깊이를 기준으로 분리해서 저장

print('split_bgr 행렬 형태 ', np.array(split_bgr).shape)
print('merge_bgr 행렬 형태', merge_bgr.shape)
#행 열 깊이 순으로 나열

print("[ch0] = \n%s" % ch0)                     # 단일 채널 원소 출력
print("[ch1] = \n%s" % ch1)
print("[ch2] = \n%s" % ch2)
print("[merge_bgr] = \n %s\n" % merge_bgr)       # 다중 채널 원소 출력

print("[split_bgr[0]] =\n%s " % split_bgr[0])
print("[split_bgr[1]] =\n%s " % split_bgr[1])
print("[split_bgr[2]] =\n%s " % split_bgr[2]) # 아까 나눈 split_bgr 출력. 단일채널 원소처럼 출력됨