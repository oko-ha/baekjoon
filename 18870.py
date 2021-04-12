# https://www.acmicpc.net/problem/18870
# 이름 : 좌표 압축
# 번호 : 18870
# 난이도 : 실버 II
# 분류 : 정렬, 값 / 좌표 압축

import sys
import copy
n = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().split()))
tempArr = copy.deepcopy(arr)
tempArr.sort()
dic = {}
i = 0
for t in tempArr:
    if t not in dic:
        dic[t] = i
        i += 1
for a in arr:
    print(dic[a], end=' ')