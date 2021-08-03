# https://www.acmicpc.net/problem/1244
# 이름 : 스위치 켜고 끄기
# 번호 : 1244
# 난이도 : 실버 IV
# 분류 : 구현, 시뮬레이션

import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
def swap(x):
    arr[x - 1] = 0 if arr[x - 1] == 1 else 1
for _ in range(int(input())):
    a, b = map(int, input().split())
    if a == 1:
        for i in range(b, n + 1, b):
            swap(i)
    else:
        swap(b)
        for i in range(1, min(b, n - b + 1)):
            if arr[b + i - 1] == arr[b - i - 1]:
                swap(b + i)
                swap(b - i)
            else:
                break
for i in range(0, n, 20):
    print(*arr[i:i+20])