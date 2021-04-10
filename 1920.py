# https://www.acmicpc.net/problem/1920
# 이름 : 수 찾기
# 번호 : 1920
# 난이도 : 실버 IV
# 분류 : 이분 탐색

from sys import stdin
n = int(stdin.readline().rstrip())
dic = dict.fromkeys(list(map(int, stdin.readline().split())))
m = int(stdin.readline().rstrip())
arr = list(map(int, stdin.readline().split()))
for i in arr:
    if i in dic:
        print(1)
    else:
        print(0)