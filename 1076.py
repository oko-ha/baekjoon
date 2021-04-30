# https://www.acmicpc.net/problem/1076
# 이름 : 저항
# 번호 : 1076
# 난이도 : 브론즈 II
# 분류 : 구현

val = {'black': 0, 'brown': 1, 'red': 2, 'orange': 3, 'yellow': 4, 'green': 5, 'blue': 6, 'violet': 7, 'grey': 8, 'white': 9}
mul = {'black': 1, 'brown': 10, 'red': 100, 'orange': 1000, 'yellow': 10000, 'green': 100000, 'blue': 1000000, 'violet': 10000000, 'grey': 100000000, 'white': 1000000000}
print((val[input()]*10+val[input()])*mul[input()])