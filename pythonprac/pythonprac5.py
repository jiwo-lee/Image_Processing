kor = [30,20,100,80,20]

for i in range(5):
    #range(시작점, 끝점, 증가량)이지만 시작점과 증가량은 생략 가능
    print(kor[i])

for i in kor:
    print(i) #바로 배열도 가능

for i in "Hello":
    print(i) #문자열도 가능
