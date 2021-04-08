# https://www.acmicpc.net/problem/10773
# 이름 : 제로
# 번호 : 10773
# 난이도 : 실버 IV
# 분류 : 구현, 자료 구조, 문자열, 스택

stack = []
for _ in range(int(input())):
    n = int(input())
    if n != 0:
        stack.append(n)
    else:
        stack.pop(-1)
print(sum(stack))