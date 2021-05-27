# https://www.acmicpc.net/problem/9375
# 이름 : 패션왕 신해빈
# 번호 : 9375
# 난이도 : 실버 III
# 분류 : 자료 구조, 문자열, 해시를 사용한 집합과 맵

import sys
from collections import Counter
input = sys.stdin.readline
for _ in range(int(input())):
    category = []
    for _ in range(int(input())):
        x, name = input().split()
        category.append(name)
    dic = Counter(category)
    ans = 1
    for d in dic:
        ans *= dic[d] + 1
    print(ans - 1)