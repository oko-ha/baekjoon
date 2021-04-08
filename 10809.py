# 알파벳 찾기
s = input()
h = {}
for i in range(26):
    h[chr(i+97)] = -1

for i in range(len(s)):
    if h[s[i]] == -1:
        h[s[i]] = i

ans = ''
for i in h.values():
    ans += str(i) + ' '
print(ans[:-1])