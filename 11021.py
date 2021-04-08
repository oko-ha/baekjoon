# https://www.acmicpc.net/problem/11021
# 이름 : A+B -7
# 번호 : 11021
# 난이도 : 브론즈 III
# 분류 : 수학, 구현, 사칙연산

n = int(input())
ans = []
for i in range(n):
    ans.append(sum(map(int, input().split())))
for i, a in enumerate(ans):
    print('Case #{}: {}'.format(i+1, a))