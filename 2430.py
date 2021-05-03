# https://www.acmicpc.net/problem/2530
# 이름 : 인공지능 시계
# 번호 : 2530
# 난이도 : 브론즈 IV
# 분류 : 수학, 사칙연산

import sys
time = list(map(int, sys.stdin.readline().split()))
unit = [24, 60, 60]
d = int(sys.stdin.readline().rstrip())
n = [d // 3600, (d % 3600) // 60, d % 60]
for i in range(2, -1, -1):
    temp = time[i] + n[i]
    time[i] = temp % unit[i]
    if i != 0:
        time[i - 1] += temp // unit[i]
print(*time)