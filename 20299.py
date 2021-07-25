# https://www.acmicpc.net/problem/20299
# 이름 : 3대 측정
# 번호 : 20299
# 난이도 : 브론즈 II
# 분류 : 구현

import sys
input = sys.stdin.readline
N, K, L = map(int, input().split())
def cond(team):
    if sum(team) >= K:
        for i in team:
            if i < L:
                return False
    else:
        return False
    return True
ans = []
for _ in range(N):
    team = list(map(int, input().split()))
    if cond(team):
        ans += team
print(len(ans) // 3)
print(*ans)