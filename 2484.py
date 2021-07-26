# https://www.acmicpc.net/problem/2484
# 이름 : 주사위 네개
# 번호 : 2484
# 난이도 : 브론즈 II
# 분류 : 수학, 구현

import sys
from collections import Counter
input = sys.stdin.readline
N = int(input())
ans = 0
for _ in range(N):
    dic = Counter(map(int, input().split())).most_common()
    if dic[0][1] == 4:
        ans = max(ans, 50000 + dic[0][0] * 5000)
    elif dic[0][1] == 3:
        ans = max(ans, 10000 + dic[0][0] * 1000)
    elif dic[0][1] == 2:
        if dic[1][1] == 2:
            ans = max(ans, 2000 + dic[0][0] * 500  + dic[1][0] * 500)
        else:
            ans = max(ans, 1000 + dic[0][0] * 100)
    else:
        ans = max(ans, max(dic[i][0] for i in range(4)) * 100)
print(ans)