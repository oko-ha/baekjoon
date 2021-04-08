# 달팽이는 올라가고 싶다
import sys
import math
a, b, c = map(int, sys.stdin.readline().split())

i = math.ceil((c - a) / (a - b))
print(i + 1)