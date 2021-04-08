import re
a = input()
s = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
for i in range(len(s)):
    a = re.sub(s[i], '!', a)
print(len(a))