# https://www.acmicpc.net/problem/1931
# 이름 : 회의실 배정
# 번호 : 1931
# 난이도 : 실버 II
# 분류 : 그리디 알고리즘, 정렬

import sys
n = int(sys.stdin.readline().rstrip())
confs = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
confs = sorted(confs, key=lambda x:[x[1], x[0]])
cnt = 0
last = 0
for conf in confs:
    if conf[0] >= last:
        cnt += 1
        last = conf[1]
print(cnt)