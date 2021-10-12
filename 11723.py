# https://www.acmicpc.net/problem/11723
# 이름 : 집합
# 번호 : 11723
# 난이도 : 실버 V
# 분류 : 구현, 비트마스킹

import sys
input = sys.stdin.readline
S = 0
for _ in range(int(input())):
    cmd = list(input().split())
    if cmd[0] == 'add':
        S |= (1 << int(cmd[1]) - 1)
    elif cmd[0] == 'remove':
        S &= ~(1 << int(cmd[1]) - 1)
    elif cmd[0] == 'check':
        if S & (1 << int(cmd[1]) - 1):
            print(1)
        else:
            print(0)
    elif cmd[0] == 'toggle':
        S ^= (1 << int(cmd[1]) - 1)
    elif cmd[0] == 'all':
        S = (1 << 20) - 1
    elif cmd[0] == 'empty':
        S = 0