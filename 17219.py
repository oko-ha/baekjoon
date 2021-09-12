# https://www.acmicpc.net/problem/17219
# 이름 : 비밀번호 찾기
# 번호 : 17219
# 난이도 : 실버 IV
# 분류 : 자료 구조, 해시를 사용한 집합과 맵

import sys
input = sys.stdin.readline
N, M = map(int, input().split())
password = {}
for _ in range(N):
    id, pw = input().split()
    password[id] = pw
for _ in range(M):
    id = input().strip()
    print(password[id])