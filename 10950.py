n = int(input())
ans = []
for i in range(n):
    ans.append(sum(map(int, input().split())))
for i in ans:
    print(i)