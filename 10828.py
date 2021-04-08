# https://www.acmicpc.net/problem/10828
# 이름 : 스택
# 번호 : 10828
# 난이도 : 실버 IV
# 분류 : 자료 구조, 스택

import sys

stack = []
for _ in range(int(sys.stdin.readline().rstrip())):
    order = sys.stdin.readline().split()
    if order[0] == 'push':
        stack.append(order[1])
    elif order[0] == 'pop':
        try:
            print(stack.pop(-1))
        except:
            print(-1)
    elif order[0] == 'size':
        print(len(stack))
    elif order[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif order[0] == 'top':
        try:
            print(stack[-1])
        except:
            print(-1)