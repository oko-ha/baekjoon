import sys
import math
a, b, c = map(int, sys.stdin.readline().split())

i = math.ceil((c - a) / (a - b))
print(i + 1)