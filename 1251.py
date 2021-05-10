# https://www.acmicpc.net/problem/1251
# 이름 : 단어 나누기
# 번호 : 1251
# 난이도 : 실버 V
# 분류 : 문자열, 브루트포스 알고리즘, 정렬

import sys
from itertools import combinations
s = sys.stdin.readline().rstrip()
arr = [i for i in range(1, len(s))]
prob = list(combinations(arr, 2))
ans = []
for p in prob:
    temp = s[:p[0]][::-1] + s[p[0]:p[1]][::-1] + s[p[1]:][::-1]
    ans.append(temp)
ans.sort()
print(ans[0])