# https://www.acmicpc.net/problem/1946
# 이름 : 신입 사원
# 번호 : 1946
# 난이도 : 실버 I
# 분류 : 그리디 알고리즘, 정렬

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    arr = []
    for _ in range(int(input())):
        a, b = map(int, input().split())
        arr.append((a, b))
    arr.sort()
    m = arr[0][1]
    ans = 1
    for i in range(1, len(arr)):
        if arr[i][1] < m:
            m = arr[i][1]
            ans += 1
    print(ans)