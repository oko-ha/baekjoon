# 상수
a, b = input().split()
a = int(a[2] + a[1] + a[0])
b = int(b[2] + b[1] + b[0])
if a > b:
    print(a)
else:
    print(b)