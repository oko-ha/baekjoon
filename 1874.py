# https://www.acmicpc.net/problem/1874
# 이름 : 스택 수열
# 번호 : 1874
# 난이도 : 실버 III
# 분류 : 자료 구조, 스택

import sys
numbers = []
n = []
for i in range(int(sys.stdin.readline().rstrip())):
    numbers.append(int(sys.stdin.readline().rstrip()))
    n.append(i + 1)
stack =[]
ans = []
for i in numbers:
    while True:
        if len(stack) != 0:
            if i == stack[-1]:
                break
        if len(n) == 0:
            print('NO')
            sys.exit()
        stack.append(n.pop(0))
        ans.append('+')
    stack.pop(-1)
    ans.append('-')

for i in ans:
    print(i)