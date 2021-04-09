# https://www.acmicpc.net/problem/2493
# 이름 : 탑
# 번호 : 2493
# 난이도 : 골드 V
# 분류 : 자료 구조, 스택

import sys
n = int(sys.stdin.readline().rstrip())
towers = list(map(int, sys.stdin.readline().split()))
stackTower = []
stackIndex = []
ans = [0] * n
tempTower = 0
tempIndex = 0
for i in range(n):
    if tempTower > towers[i]:
        ans[i] = tempIndex
    else:
        while stackTower:
            tempTower = stackTower.pop()
            tempIndex = stackIndex.pop()
            if tempTower > towers[i]:
                ans[i] = tempIndex
                break
    if i < n - 1:
        if towers[i] > towers[i + 1]:
            if tempTower != 0:
                stackTower.append(tempTower)
                stackIndex.append(tempIndex)
            tempTower = towers[i]
            tempIndex = i + 1
print(*ans)