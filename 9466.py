# https://www.acmicpc.net/problem/9466
# 이름 : 텀 프로젝트
# 번호 : 9466
# 난이도 : 골드 IV
# 분류 : 그래피 이론, 그래프 탐색, 깊이 우선 탐색

import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    arr = [0] + list(map(int, input().split()))
    ans = 0
    for i in range(1, n + 1):
        node = i
        visit = {node:0}
        cnt = 1
        while True:
            if arr[node] > 0 and arr[node] not in visit:
                temp = node
                node = arr[node]
                arr[temp] = 0
                visit[node] = cnt
                cnt += 1
            elif arr[node] == 0:
                ans += visit[node]
                break
            elif arr[node] in visit:
                ans += visit[arr[node]]
                arr[node] = 0
                break
    print(ans)