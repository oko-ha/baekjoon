# https://www.acmicpc.net/problem/1966
# 이름 : 프린터 큐
# 번호 : 1966
# 난이도 : 실버 III
# 분류 : 구현, 자료 구조, 시뮬레이션, 큐

from sys import stdin
from collections import deque
for _ in range(int(stdin.readline().rstrip())):
    n, location = map(int, stdin.readline().split())
    queue = deque([(i, p) for i, p in enumerate(list(map(int, stdin.readline().split())))])
    answer = 0
    while True:
        cur = queue.popleft()
        if any(cur[1] < q[1] for q in queue):
            queue.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                print(answer)
                break