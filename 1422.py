# https://www.acmicpc.net/problem/1422
# 이름 : 숫자의 신
# 번호 : 1422
# 난이도 : 플래티넘 V
# 분류 : 그리디 알고리즘, 정렬

import sys
from functools import cmp_to_key
input = sys.stdin.readline
K, N = map(int, input().split())
num, m = [], 0
for _ in range(K):
    x = int(input())
    if x > m:
        m = x
    num.append(str(x))
def comp(x, y):
    if x == y:
        return 0
    elif int(x + y) < int(y + x):
        return 1
    else:
        return -1
num = sorted(num, key=cmp_to_key(comp))
ans = ''
flag = True
for n in num:
    if n == str(m) and flag:
        for _ in range(N - K):
            ans += n
        flag = False
    ans += n
print(ans)