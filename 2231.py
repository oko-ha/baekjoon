# https://www.acmicpc.net/problem/2231
# 이름 : 분해합
# 번호 : 2231
# 난이도 : 브론즈 II
# 분류 : 브루트포스 알고리즘

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