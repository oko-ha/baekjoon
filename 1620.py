# https://www.acmicpc.net/problem/1620
# 이름 : 나는야 포켓몬 마스터 이다솜
# 번호 : 1620
# 난이도 : 실버 IV
# 분류 : 자료 구조, 해시를 사용한 집합과 맵

import sys
input = sys.stdin.readline
N, M = map(int, input().split())
name = {}
num = {}
for i in range(1, N + 1):
    s = input().strip()
    name[s] = i
    num[i] = s
for _ in range(M):
    s = input().strip()
    if s[0].isalpha():
        print(name[s])
    else:
        print(num[int(s)])