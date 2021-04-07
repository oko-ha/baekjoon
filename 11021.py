n = int(input())
ans = []
for i in range(n):
    ans.append(sum(map(int, input().split())))
for i, a in enumerate(ans):
    print('Case #{}: {}'.format(i+1, a))