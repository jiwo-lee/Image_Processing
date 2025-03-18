import numpy as np

np.random.seed(10)
a = np.random.rand(3,4) #0~1까지 랜덤 3행 4열 크기로
b = np.random.randn(3,2) #평균 0 표준편차 1의 랜덤 3행 4열 크기로
c = np.random.rand(36) #한줄로 랜덤 36개
d = np.random.randint(1,100,12) # 1부터 100까지 정수 12개 한줄로

c = np.reshape(c, (9,4)) #c를 9행 4열로 변경
d = d.reshape(3,-1) #d를 3행에 맞춰서 알아서 변경

print(a.flatten()) #a를 한줄로
print(np.ravel(b)) #b를 한줄로
print(np.reshape(c,(-1,))) #c를 한줄로
print(d.reshape(-1,)) #d를 한줄로