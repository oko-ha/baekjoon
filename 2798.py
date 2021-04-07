from itertools import combinations

n, m = map(int, input().split())
lst = list(map(int, input().split()))
cb = list(combinations(lst,3))
ans = []
for i in cb:
    if sum(i) <= m:
        ans.append(sum(i))
print(max(ans))