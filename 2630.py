# https://www.acmicpc.net/problem/2630
# 이름 : 색종이 만들기
# 번호 : 2630
# 난이도 : 실버 III
# 분류 : 분할 정복, 재귀

import sys
n = int(sys.stdin.readline().rstrip())
arr = []
for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))
def isWhite(arr):
    s = 0
    for i in arr:
        s += sum(i)
    return s == 0
def isBlue(arr):
    s = 0
    for i in arr:
        s += sum(i)
    return s == len(arr) * len(arr)
def paper(arr):
    global blue
    global white
    if isWhite(arr):
        white += 1
    elif isBlue(arr):
        blue += 1
    else:
        if len(arr) > 1:
            k = len(arr) // 2
            tempArr = [arr[i][:k] for i in range(k)]
            paper(tempArr)
            tempArr = [arr[i][k:] for i in range(k)]
            paper(tempArr)
            tempArr = [arr[i][:k] for i in range(k, len(arr))]
            paper(tempArr)
            tempArr = [arr[i][k:] for i in range(k, len(arr))]
            paper(tempArr)
white = 0
blue = 0
paper(arr)
print(white, blue)