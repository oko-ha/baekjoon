# https://www.acmicpc.net/problem/11652
# 이름 : 카드
# 번호 : 11652
# 난이도 : 실버 IV
# 분류 : 자료 구조, 정렬, 해시를 사용한 집합과 맵

import sys
from collections import defaultdict
input = sys.stdin.readline

d = defaultdict(int)
for _ in range(int(input())):
    n = int(input())
    d[n] += 1
print(sorted(d.items(), key=lambda x: (-x[1], x[0]))[0][0])