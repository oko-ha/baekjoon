# https://www.acmicpc.net/problem/11022
# 이름 : A+B -8
# 번호 : 11022
# 난이도 : 브론즈 III
# 분류 : 수학, 구현, 사칙연산

n = int(input())
ans = []
for i in range(n):
    ans.append(list(map(int, input().split())))
for i, a in enumerate(ans):
    print('Case #{}: {} + {} = {}'.format(i+1, a[0], a[1], a[0]+a[1]))