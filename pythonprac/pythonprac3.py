#슬라이스 연산자 [시작:끝(끝 - 1까지만 바뀜):증가폭(디폴트는 1, 역순은 음수)]

a = [0,1,2,3,4,5,6,7,8,9]

print(a)
print(a[:2]) #== print(a[0:2:1]) 01
print(a[4:-1]) #4부터 마지막 -1(즉, 8. 왜냐면 9는 포함안하니까)까지 == print(a[4:9]) 45678
print(a[2::2]) #2부터 9까지 2만큼 증가 == print(a[2:10:2]) 2468
print(a[::-1]) #처음부터 끝까지 역순으로 9876543210
print(a[1::-1]) #1부터 시작하는데 역순으로 10
print(a[7:1-2]) #7부터 시작해서 1의 전까지 역순으로 2만큼 753
print(a[:-4:1]) #맨 마지막부터 마지막 -4(즉, 7. 왜냐면 6은 포함 안하니까)까지 역순 987