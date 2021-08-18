# https://www.acmicpc.net/problem/2922
# 이름 : 즐거운 단어
# 번호 : 2922
# 난이도 : 골드 IV
# 분류 : 문자열, 브루트포스 알고리즘, 백트래킹

import sys
word = list(sys.stdin.readline().strip())
blank = []
def check(x):
    left = max(0, x - 2)
    right = min(len(word), x + 3)
    mo = ja = 0
    for w in word[left:right]:
        if w == '_':
            mo = ja = 0
        elif w in {'A', 'E', 'I', 'O', 'U', '2'}:
            mo += 1
            ja = 0
        else:
            ja += 1
            mo = 0
        if mo > 2 or ja > 2:
            return False
    return True
def mul(arr):
    m = 1
    for a in arr:
        m *= a
    return m
temp = []
ans = []
prob = {0:20, 1:1, 2:5}
def backtracking(k):
    if k < len(blank):
        for i in range(3):
            word[blank[k]] = str(i)
            if check(blank[k]):
                temp.append(prob[i])
                backtracking(k + 1)
                temp.pop()
            word[blank[k]] = '_'
    else:
        if lFlag or (1 in temp):
            ans.append(mul(temp))

def conf():
    global lFlag
    lFlag = False
    mo = ja = 0
    for i in range(len(word)):
        if word[i] == '_':
            blank.append(i)
            mo = ja = 0
        elif word[i] in {'A', 'E', 'I', 'O', 'U'}:
            mo += 1
            ja = 0
        elif word[i] == 'L':
            ja += 1
            mo = 0
            lFlag = True
        else:
            ja += 1
            mo = 0
        if mo > 2 or ja > 2:
            return 0
    if len(blank):
        backtracking(0)
        return sum(ans)
    else:
        if lFlag:
            return 1
        else:
            return 0
print(conf())