# https://www.acmicpc.net/problem/1003
# 이름 : 피보나치 함수
# 번호 : 1003
# 난이도 : 실버 III
# 분류 : 다이나믹 프로그래밍

import sys
arr = [[1, 0], [0, 1]]
for _ in range(int(sys.stdin.readline().rstrip())):
    n = int(sys.stdin.readline().rstrip())
    try:
        print(' '.join(map(str, arr[n])))
    except:
        for i in range(len(arr), n + 1):
            arr.append([arr[i - 2][0] + arr[i - 1][0], arr[i - 2][1] + arr[i - 1][1]])
        print(' '.join(map(str, arr[n])))