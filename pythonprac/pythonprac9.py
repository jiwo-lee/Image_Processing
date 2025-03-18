import numpy as np

list1, list2 = [1,2,3,4], [5,6,7,8]

a = np.array(list1)
b = np.array(list2)

c = a + b
d = a - b
e = a * b
f = a / b
g = b // a
h = b % a
i = a ** 2
j = b + 2

print(c, d, e, f)
print(g,h,i,j)

a1 = np.zeros((2,5), np.int_) #2행 5열, 32비트 정수형
b1 = np.ones((3,2), np.uint8) #8비트 unsigned 정수형
c1 = np.empty((1,5), np.float_) #64비트 실수형
d1 = np.full((3,3), 15, np.float32) #32비트 실수형

print(a1)
print(b1)
print(c1)
print(d1)