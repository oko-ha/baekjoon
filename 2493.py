# https://www.acmicpc.net/problem/2493
# 이름 : 탑
# 번호 : 2493
# 난이도 : 골드 V
# 분류 :

import sys
n = int(sys.stdin.readline().rstrip())
towers = list(map(int, sys.stdin.readline().split()))
stackTower = []
stackIndex = []
ans = [0] * n
tempTower = 0
tempIndex = 0
for i in range(n):
    tower = towers.pop(0)
    if tempTower >= tower:
        ans[i] = tempIndex
    else:
        while stackTower:
            tempTower = stackTower.pop()
            tempIndex = stackIndex.pop()
            if tempTower > tower:
                ans[i] = tempIndex
                stackTower.append(tempTower)
                stackIndex.append(tempIndex)
                break
    if len(towers) != 0:
        if tower > towers[0]:
            tempTower = tower
            tempIndex = i + 1
    stackTower.append(tower)
    stackIndex.append(i + 1)
print(*ans)