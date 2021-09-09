# https://www.acmicpc.net/problem/1644
# 이름 : 소수의 연속합
# 번호 : 1644
# 난이도 : 골드 III
# 분류 : 수학, 정수론, 두 포인터, 소수 판정, 에라토스테네스의 체

import sys
N = int(sys.stdin.readline())
arr = [False, False] + [True] * (N - 1)
prime = []
for i in range(2, N + 1):
    if arr[i]:
        prime.append(i)
        for j in range(2 * i, N + 1, i):
            arr[j] = False
ans = temp = 0
i = -1
for j in range(len(prime)):
    temp += prime[j]
    if temp > N:
        while i < j and temp > N:
            i += 1
            temp -= prime[i]
    if temp == N:
        ans += 1
print(ans)