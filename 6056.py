i, h = input().split()
i = bool(int(i))
h = bool(int(h))
print((i and (not h)) or ((not i) and h))
