# https://www.acmicpc.net/problem/2622
# 이름 : 삼각형만들기
# 번호 : 2622
# 난이도 : 브론즈 II
# 분류 : 수학

import sys
n = int(sys.stdin.readline())
cnt = 0
for a in range(1, n // 2 + 1):
    for b in range(a, n // 2 + 1):
        c = n - a - b
        if b > c:
            break
        if a + b > c:
            cnt += 1
print(cnt)