# https://www.acmicpc.net/problem/2798
# 이름 : 블랙잭
# 번호 : 2798
# 난이도 : 브론즈 II
# 분류 : 브루트포스 알고리즘

from itertools import combinations

n, m = map(int, input().split())
lst = list(map(int, input().split()))
cb = list(combinations(lst,3))
ans = []
for i in cb:
    if sum(i) <= m:
        ans.append(sum(i))
print(max(ans))