# https://www.acmicpc.net/problem/2775
# 이름 : 부녀회장이 될테야
# 번호 : 2775
# 난이도 : 브론즈 II
# 분류 : 수학, 조합론

from sys import stdin
for _ in range(int(stdin.readline().strip())):
    k = int(stdin.readline().rstrip())
    n = int(stdin.readline().rstrip())
    arr = [i for i in range(1, n + 1)]
    for i in range(k):
        for j in range(1, n):
            arr[j] += arr[j - 1]
    print(arr[-1])