# https://www.acmicpc.net/problem/14425
# 이름 : 문자열 집합
# 번호 : 14425
# 난이도 : 실버 II
# 분류 : 자료 구조, 문자열, 트리, 트리를 사용한 집합과 맵, 해시를 사용한 집합과 맵, 트라이

import sys
input = sys.stdin.readline
N, M = map(int, input().split())
S = {input().strip() for _ in range(N)}
ans = 0
for _ in range(M):
    if input().strip() in S:
        ans += 1
print(ans)