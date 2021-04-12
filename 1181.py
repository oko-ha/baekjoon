# https://www.acmicpc.net/problem/1181
# 이름 : 단어 정렬
# 번호 : 1181
# 난이도 : 실버 V
# 분류 : 문자열, 정렬

import sys
wordDict = {}
for _ in range(int(sys.stdin.readline().rstrip())):
    w = sys.stdin.readline().rstrip()
    if w not in wordDict:
        wordDict[w] = len(w)
words = sorted(list(zip(wordDict.keys(), wordDict.values())), key=lambda x : (x[1], x[0]))
for word in words:
    print(word[0])