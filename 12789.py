# https://www.acmicpc.net/problem/12789
# 이름 : 도키도키 간식드리미
# 번호 : 12789
# 난이도 : 실버 IV
# 분류 : 자료 구조, 스택

import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
students = deque(map(int, input().split()))

index = 1
stack = []
while index <= N:
    if students and index == students[0]:
        index += 1
        students.popleft()
    elif stack and index == stack[-1]:
        index += 1
        stack.pop()
    else:
        if not students:
            break
        else:
            stack.append(students.popleft())
if index > N:
    print('Nice')
else:
    print('Sad')