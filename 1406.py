# https://www.acmicpc.net/problem/1406
# 이름 : 에디터
# 번호 : 1406
# 난이도 : 실버 III
# 분류 : 자료 구조, 스택

import sys
input = sys.stdin.readline
left = list(input().rstrip())
right = []
for _ in range(int(input())):
    cmd = list(input().split())
    if cmd[0] == 'L':
        if left:
            right.append(left.pop())
    elif cmd[0] == 'D':
        if right:
            left.append(right.pop())
    elif cmd[0] == 'B':
        if left:
            left.pop()
    elif cmd[0] == 'P':
        left.append(cmd[1])
right.reverse()
print(''.join(left + right))