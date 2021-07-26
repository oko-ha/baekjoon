# https://www.acmicpc.net/problem/1924
# 이름 : 2007년
# 번호 : 1924
# 난이도 : 브론즈 I
# 분류 : 구현

import sys
x, y = map(int, sys.stdin.readline().split())
month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
arr = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
print(arr[(sum(month[:x]) + y - 1) % 7])