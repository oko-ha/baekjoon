# https://www.acmicpc.net/problem/1755
# 이름 : 숫자놀이
# 번호 : 1755
# 난이도 : 실버 V
# 분류 : 수학, 정렬

import sys
m, n = map(int, sys.stdin.readline().split())
num_text = {'0':'zero', '1':'one', '2':'two', '3':'three', '4':'four', \
    '5':'five', '6':'six', '7':'seven', '8':'eight', '9':'nine'}
text_num = {'zero':'0', 'one':'1', 'two':'2', 'three':'3', 'four':'4', \
    'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}

s = []
for i in range(m, n+1):
    if len(str(i)) == 2:
        s.append(num_text[str(i)[0]] + ' ' + num_text[str(i)[1]])
    else:
        s.append(num_text[str(i)])
s.sort()
line = 0
for i in s:
    temp = i.split()
    ans = ''
    for t in temp:
        ans += text_num[t]
    print(ans, end=' ')
    line += 1
    if line % 10 == 0:
        print()