# https://www.acmicpc.net/problem/1654
# 이름 : 랜선 자르기
# 번호 : 1654
# 난이도 : 실버 III
# 분류 : 이분 탐색, 매개 변수 탐색

import sys
import math
k, n = map(int, sys.stdin.readline().split())
numbers = []
max = -1
for _ in range(k):
    numbers.append(int(sys.stdin.readline().rstrip()))
    if numbers[-1] > max:
        max = numbers[-1]

def isN(i):
    s = 0
    for number in numbers:
        s += math.floor(number / i)
    return s < n

ans = 1
left, right = 0, max + 1
while left + 1 < right:
    mid = math.ceil((left + right) / 2)
    if isN(mid):
        right = mid
    else:
        left = mid
        if mid > ans:
            ans = mid
print(ans)