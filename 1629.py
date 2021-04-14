# https://www.acmicpc.net/problem/1629
# 이름 : 곱셈
# 번호 : 1629
# 난이도 : 실버 I
# 분류 : 수학, 분할 정복을 이용한 거듭제곱

import sys
a, b, c = map(int, sys.stdin.readline().split())
arr = [a]
def mod(n):
    if n <= b:
        arr.append(arr[-1] ** 2 % c)
        mod(n * 2)
mod(2)
ans = 1
for i in list(bin(b)[2:]):
    if i == '1':
        ans = (ans * arr.pop()) % c
    else:
        arr.pop()
print(ans)