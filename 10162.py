# https://www.acmicpc.net/problem/10162
# 이름 : 전자레인지
# 번호 : 10162
# 난이도 : 브론즈 IV
# 분류 : 수학, 구현, 그리디 알고리즘

import sys
T = int(sys.stdin.readline())
time = [300, 60, 10]
ans = [0, 0, 0]
for i in range(3):
    ans[i] = T // time[i]
    T %= time[i]
if T > 0:
    print(-1)
else:
    print(*ans)