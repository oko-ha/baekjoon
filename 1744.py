# https://www.acmicpc.net/problem/1744
# 이름 : 수 묶기
# 번호 : 1744
# 난이도 : 골드 IV
# 분류 : 그리디 알고리즘, 정렬

import sys
input = sys.stdin.readline
m, p, o, z = [], [], 0, 0
for _ in range(int(input())):
    n = int(input())
    if n < 0:
        m.append(n)
    elif n > 1:
        p.append(n)
    elif n == 1:
        o += 1
    else:
        z += 1
m, p = sorted(m, reverse=True), sorted(p)
ans = o
while m:
    if len(m) == 1:
        if z == 0:
            ans += m.pop()
        else:
            m.pop()
    else:
        ans += m.pop() * m.pop()
while p:
    if len(p) == 1:
        ans += p.pop()
    else:
        ans += p.pop() * p.pop()
print(ans)