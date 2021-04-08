# A+B -8
n = int(input())
ans = []
for i in range(n):
    ans.append(list(map(int, input().split())))
for i, a in enumerate(ans):
    print('Case #{}: {} + {} = {}'.format(i+1, a[0], a[1], a[0]+a[1]))