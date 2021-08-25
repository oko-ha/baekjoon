# https://www.acmicpc.net/problem/1342
# 이름 : 행운의 문자열
# 번호 : 1342
# 난이도 : 실버 I
# 분류 : 브루트포스 알고리즘, 백트래킹

import sys
from collections import Counter
s = sys.stdin.readline().strip()
dic = Counter(s)
def dfs(w, k):
    global ans
    if k < len(s):
        for d in dic:
            if w != d and dic[d] > 0:
                dic[d] -= 1
                dfs(d, k + 1)
                dic[d] += 1
    else:
        ans += 1
ans = 0
dfs('', 0)
print(ans)