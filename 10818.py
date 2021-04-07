lst = []
for i in range(9):
    lst.append(int(input()))
print(max(lst), lst.index(max(lst)) + 1)