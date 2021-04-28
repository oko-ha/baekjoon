# https://www.acmicpc.net/problem/7568
# 이름 : 덩치
# 번호 : 7568
# 난이도 : 실버 V
# 분류 : 구현, 브루트포스 알고리즘

import sys
n = int(sys.stdin.readline().rstrip())
people = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
ans = [1] * n
for i in range(n):
    for j in range(n):
        if i != j:
            if people[i][0] < people[j][0] and people[i][1] < people[j][1]:
                ans[i] += 1
print(*ans)