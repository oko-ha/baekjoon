# https://www.acmicpc.net/problem/11726
# 이름 : 2xn 타일링
# 번호 : 11726
# 난이도 : 실버 III
# 분류 : 다이나믹 프로그래밍

import sys
n = int(sys.stdin.readline())
arr = [0, 1, 2]
for i in range(3, n + 1):
    arr.append(arr[i-2] + arr[i-1])
print(arr[n] % 10007)