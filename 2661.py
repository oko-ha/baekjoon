# https://www.acmicpc.net/problem/2661
# 이름 : 좋은수열
# 번호 : 2661
# 난이도 : 골드 IV
# 분류 : 백트래킹

import sys
n = int(sys.stdin.readline())
arr = [1]
def check():
    if len(arr) % 2 == 0:
        for i in range(0, len(arr), 2):
            x = i + (len(arr) - i + 1) // 2
            if arr[i:x] == arr[x:]:
                return False
    else:
        for i in range(1, len(arr), 2):
            x = i + (len(arr) - i + 1) // 2
            if arr[i:x] == arr[x:]:
                return False
    return True
def backtracking(k):
    if k < n:
        for i in range(1, 4):
            arr.append(i)
            if check():
                backtracking(k + 1)
            arr.pop()
    else:
        print(''.join(map(str, arr)))
        exit(0)
backtracking(1)