# https://www.acmicpc.net/problem/1718
# 이름 : 암호
# 번호 : 1718
# 난이도 : 브론즈 II
# 분류 : 문자열

import sys
plain = sys.stdin.readline().rstrip()
key = sys.stdin.readline().rstrip()
cipher = ''
for i in range(len(plain)):
    if plain[i] == ' ':
        cipher += ' '
    else:
        cipher += chr(((ord(plain[i]) - ord(key[i % len(key)]) - 1) % 26) + 97)
print(cipher)