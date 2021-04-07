n = input()
l = len(n)
n = int(n)
ans = 0
for i in range(l, n):
    sum = i
    for j in str(i):
        sum += int(j)
    if sum == n:
        ans = i
        break
print(ans)