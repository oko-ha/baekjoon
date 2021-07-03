# https://www.acmicpc.net/problem/2669
# 이름 : 직사각형 네개의 합집합의 면적 구하기
# 번호 : 2669
# 난이도 : 브론즈 I
# 분류 : 구현

import sys
arr = [[0 for _ in range(101)] for _ in range(101)]
for _ in range(4):
    x0, y0, x1, y1 = map(int, sys.stdin.readline().split())
    for i in range(x0, x1):
        for j in range(y0, y1):
            arr[i][j] = 1
ans = 0
for a in arr:
    ans += sum(a)
print(ans)