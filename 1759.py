# https://www.acmicpc.net/problem/1759
# 이름 : 암호 만들기
# 번호 : 1759
# 난이도 : 골드 V
# 분류 : 수학, 브루트포스 알고리즘, 조합론, 백트래킹

import sys
input = sys.stdin.readline
L, C = map(int, input().split())
arr = sorted(list(input().split()))
check = [0 ,0]
ans = []
def backtracking(k, a):
    if k < L:
        for i in range(a, C):
            if arr[i] in {'a', 'e', 'i', 'o', 'u'}:
                temp = 0
            else:
                temp = 1
            ans.append(arr[i])
            check[temp] += 1
            backtracking(k + 1, i + 1)
            ans.pop()
            check[temp] -= 1
    else:
        if check[0] > 0 and check[1] > 1:
            print(''.join(ans))
backtracking(0, 0)