# https://www.acmicpc.net/problem/1083
# 이름 : 소트
# 번호 : 1083
# 난이도 : 골드 IV
# 분류 : 그리디 알고리즘, 정렬

import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
S = int(input())
cnt = 0
while S > 0 and cnt < len(arr):
    index = arr.index(max(arr[cnt:min(len(arr), S+cnt+1)]))
    for i in range(index, cnt, -1):
        temp = arr[i]
        arr[i] = arr[i - 1]
        arr[i - 1] = temp
    S -= index - cnt
    cnt += 1
print(*arr)