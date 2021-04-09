# https://www.acmicpc.net/problem/17298
# 이름 : 오큰수
# 번호 : 17298
# 난이도 : 골드 IV
# 분류 : 자료 구조, 스택

import sys
n = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))
ans = [-1] * n
stack = []
temp = 0
for i in range(n - 2, -1, -1):
    number = numbers.pop()
    stack.append(number)
    if numbers[-1] < number:
        temp = number
    if numbers[-1] >= temp:
        while stack:
            temp = stack.pop()
            if numbers[-1] < temp:
                ans[i] = temp
                stack.append(temp)
                break
    else:
        ans[i] = temp

print(*ans)