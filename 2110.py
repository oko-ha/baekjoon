# https://www.acmicpc.net/problem/2110
# 이름 : 공유기 설치
# 번호 : 2110
# 난이도 : 실버 I
# 분류 : 이분 탐색, 매개 변수 탐색

import sys
n, c = map(int, sys.stdin.readline().split())
houses = [int(sys.stdin.readline()) for _ in range(n)]
houses.sort()
left, right = 1, houses[-1] - houses[0]

# 해당 거리를 유지하며 공유기가 몇 개 설치되는지
def getRouters(k):
    cnt = 1
    loc = houses[0] # 시작점
    for house in houses:
        if loc + k <= house: # 이전 집에서 해당 거리보다 멀리 떨어진 집이라면
            cnt += 1
            loc = house # 공유기 설치된 집 갱신
    return cnt < c

while left <= right:
    mid = (left + right) // 2
    if getRouters(mid):
        right = mid - 1
    else:
        left = mid + 1
        ans = mid
print(ans)