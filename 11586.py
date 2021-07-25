# https://www.acmicpc.net/problem/11586
# 이름 : 지영 공주님의 마법 거울
# 번호 : 11586
# 난이도 : 브론즈 I
# 분류 : 구현, 문자열

import sys
input = sys.stdin.readline
N = int(input())
arr = [list(input().strip()) for _ in range(N)]
state = int(input())
for i in range(N):
    if state == 1:
        print(''.join(arr[i]))
    elif state == 2:
        arr[i].reverse()
        print(''.join(arr[i]))
    elif state == 3:
        print(''.join(arr[N - i - 1]))