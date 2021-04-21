# https://www.acmicpc.net/problem/10816
# 이름 : 숫자 카드 2
# 번호 : 10816
# 난이도 : 실버 IV
# 분류 : 자료 구조, 이분 탐색, 해시를 사용한 집합과 맵

from sys import stdin
from collections import Counter
stdin.readline()
dic = Counter(list(map(int, stdin.readline().split())))
stdin.readline()
lst = list(map(int, stdin.readline().split()))
for i in lst:
    print(dic[i], end=' ')