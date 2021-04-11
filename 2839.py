# https://www.acmicpc.net/problem/2839
# 이름 : 설탕 배달
# 번호 : 2839
# 난이도 : 브론즈 I
# 분류 : 수학, 다이나믹 프로그래밍, 그리디 알고리즘

import sys
n = int(sys.stdin.readline().rstrip())
i = n // 5
for j in range(i, -1, -1):
    if (n - 5 * j) % 3 == 0:
        n -= 5 * j
        cnt = j
        break
if n % 3 != 0:
    print(-1)
else:
    print(cnt + n // 3)