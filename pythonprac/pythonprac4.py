year = int(input("연도를 입력하시오: ")) #string으로 값이 들어옴 따라서 int()로 int값으로 교체

if (year % 4 == 0) and (year % 100 != 0):
    print("윤년입니다.")
elif year % 400 == 0:
    print("윤년입니다.")
else:
    print("윤년이 아닙니다.")

n = 3

while n >= 0:
    m = int(input("Enter a integer: "))
    if m == 0: break
    n = n-1
else:
    print("4 input") #while에 else를 걸수가 있다