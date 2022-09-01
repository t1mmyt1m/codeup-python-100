i, h = input().split()
i = bool(int(i))
h = bool(int(h))
print(((not i) and (not h)) or (i and h))
