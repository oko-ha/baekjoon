# https://www.acmicpc.net/problem/1834
# 이름 : 나머지와 몫이 같은 수
# 번호 : 1834
# 난이도 : 브론즈 I
# 분류 : 수학

import sys
N = int(sys.stdin.readline())
ans = 0
for i in range(N + 1, N ** 2, N + 1):
    ans += i
print(ans)