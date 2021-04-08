# https://www.acmicpc.net/problem/1158
# 이름 : 요세푸스 문제
# 번호 : 1158
# 난이도 : 실버 V
# 분류 : 자료 구조, 큐

import re
n, k = map(int, input().split())

lst = [i for i in range(1, n + 1)]
index = k
ans = []
for loop in range(n):
    if index > len(lst):
        while index > len(lst):
            index -= len(lst)
        ans.append(lst.pop(index - 1))
        index -= 1
    else:
        ans.append(lst.pop(index - 1))
        index -= 1
    index += k

print(re.sub('^\[(.*)\]$', '<\\1>', str(ans)))