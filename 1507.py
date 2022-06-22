# https://www.acmicpc.net/problem/1507
# 이름 : 궁금한 민호
# 번호 : 1507
# 난이도 : 골드 II
# 분류 : 그래프 이론, 플로이드-워셜

import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
check = [[1] * N for _ in range(N)]

def floyd():
    for k in range(N):
        for i in range(N):
            for j in range(i + 1, N):
                if i == k or j == k:
                    continue
                if arr[i][j] == arr[i][k] + arr[k][j]:
                    check[i][j] = 0
                elif arr[i][j] > arr[i][k] + arr[k][j]:
                    return -1
    return 0

ans = floyd()
if ans != -1:
    for i in range(N):
        for j in range(i + 1, N):
            if check[i][j]:
                ans += arr[i][j]
print(ans)