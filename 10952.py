# https://www.acmicpc.net/problem/10952
# 이름 : A+B -5
# 번호 : 10952
# 난이도 : 브론즈 III
# 분류 : 수학, 구현, 사칙연산

ans = []
while True:
    ans.append(sum(map(int, input().split())))
    if ans[-1] == 0: break
for i in ans[:-1]:
    print(i)