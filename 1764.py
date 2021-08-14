# https://www.acmicpc.net/problem/1764
# 이름 : 듣보잡
# 번호 : 1764
# 난이도 : 실버 IV
# 분류 : 자료 구조, 문자열, 정렬, 해시를 사용한 집합과 맵

import sys
input = sys.stdin.readline
N, M = map(int, input().split())
h = set(input().strip() for _ in range(N))
ans = []
for _ in range(M):
    s = input().strip()
    if s in h:
        ans.append(s)
print(len(ans))
for a in sorted(ans):
    print(a)