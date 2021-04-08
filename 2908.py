# https://www.acmicpc.net/problem/2908
# 이름 : 상수
# 번호 : 2908
# 난이도 : 브론즈 II
# 분류 : 구현

a, b = input().split()
a = int(a[2] + a[1] + a[0])
b = int(b[2] + b[1] + b[0])
if a > b:
    print(a)
else:
    print(b)