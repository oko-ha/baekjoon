# https://www.acmicpc.net/problem/2096
# 이름 : 내려가기
# 번호 : 2096
# 난이도 : 골드 IV
# 분류 : 다이나믹 프로그래밍, 슬라이딩 윈도우

import sys
input = sys.stdin.readline

N = int(input())
a, b, c = map(int, input().split())
arr = [[a, b, c], [a, b, c]]
for _ in range(N - 1):
    a, b, c = map(int, input().split())
    arr[0] = [a + max(arr[0][0], arr[0][1]), b + max(arr[0]), c + max(arr[0][1], arr[0][2])]
    arr[1] = [a + min(arr[1][0], arr[1][1]), b + min(arr[1]), c + min(arr[1][1], arr[1][2])]
print(max(arr[0]), min(arr[1]))