# https://www.acmicpc.net/problem/1300
# 이름 : K번째 수
# 번호 : 1300
# 난이도 : 골드 III
# 분류 : 이분 탐색

import sys
n = int(sys.stdin.readline().rstrip())
k = int(sys.stdin.readline().rstrip())

def getIndex(num):
    s = 0
    for i in range(1, n+1):
        s += min(num//i, n)
    return s >= k

left, right = 1, n ** 2
while left <= right:
    mid = (left + right) // 2
    if getIndex(mid):
        ans = mid
        right = mid - 1
    else:
        left = mid + 1
print(ans)