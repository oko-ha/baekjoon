# https://www.acmicpc.net/problem/9372
# 이름 : 상근이의 여행
# 번호 : 9372
# 난이도 : 실버 IV
# 분류 : 그래프 이론, 트리

import sys
input = sys.stdin.readline
for _ in range(int(input())):
    N, M = map(int, input().split())
    for _ in range(M):
        a, b = map(int, input().split())
    print(N-1)