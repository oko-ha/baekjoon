# https://www.acmicpc.net/problem/2562
# 이름 : 최댓값
# 번호 : 2562
# 난이도 : 브론즈 II
# 분류 : 구현

lst = []
for i in range(9):
    lst.append(int(input()))
print(max(lst), lst.index(max(lst)) + 1)