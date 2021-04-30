import sys
from collections import Counter
s = Counter(list(sys.stdin.readline().rstrip().lower()))
print(s)
print(max(s))