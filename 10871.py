# https://www.acmicpc.net/problem/10871
# 이름 : X보다 작은 수
# 번호 : 10871
# 난이도 : 브론즈 III
# 분류 : 수학, 구현

a, b = map(int, input().split())
lst = list(map(int, input().split()))
for i in lst:
    if i < b:
        print(i, end=" ")