# https://www.acmicpc.net/problem/2805
# 이름 : 나무 자르기
# 번호 : 2805
# 난이도 : 실버 III
# 분류 : 이분 탐색

import sys
import math
n, m = map(int, sys.stdin.readline().split())
woods = list(map(int, sys.stdin.readline().split()))
left, right, ans = 0, max(woods), 0

def getWoods(k):
    s = 0
    for wood in woods:
        if wood - k > 0:
            s += wood - k
    return s < m

while left + 1 < right:
    mid = math.ceil((left + right) / 2)
    if getWoods(mid):
        right = mid
    else:
        left = mid
        ans = mid
print(ans)