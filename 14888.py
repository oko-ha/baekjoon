# https://www.acmicpc.net/problem/14888
# 이름 : 연산자 끼워넣기
# 번호 : 14888
# 난이도 : 실버 I
# 분류 : 브루트포스 알고리즘, 백트래킹

import sys
input = sys.stdin.readline
n = int(input())
num = list(map(int, input().split()))
a, b, c, d = map(int, input().split())
def dfs(k, val, plus, minus, mul, div):
    global max_ans
    global min_ans
    if k == n:
        max_ans = max(max_ans, val)
        min_ans = min(min_ans, val)
    if plus:
        dfs(k + 1, val + num[k], plus - 1, minus, mul, div)
    if minus:
        dfs(k + 1, val - num[k], plus, minus - 1, mul, div)
    if mul:
        dfs(k + 1, val * num[k], plus, minus, mul - 1, div)
    if div:
        dfs(k + 1, -(-val // num[k]) if val < 0 else val // num[k], plus, minus, mul, div - 1)
max_ans = -1e9 - 1
min_ans = 1e9 + 1
dfs(1, num[0], a, b, c, d)
print(max_ans)
print(min_ans)