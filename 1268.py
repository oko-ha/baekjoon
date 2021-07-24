# https://www.acmicpc.net/problem/1268
# 이름 : 임시 반장 정하기
# 번호 : 1268
# 난이도 : 브론즈 I
# 분류 : 구현

import sys
input = sys.stdin.readline
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
m = 0
ans = 1
for i in range(N):
    cnt = 0
    for j in range(N):
        if i == j:
            continue
        for k in range(5):
            if arr[i][k] == arr[j][k]:
                cnt += 1
                break
    if cnt > m:
        m = cnt
        ans = i + 1
print(ans)