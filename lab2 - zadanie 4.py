a = list(range(1, 26))
new_start=a.pop()
new_end=a.pop(0)
a.append(new_end)
a.insert(0, new_start)
print(a)