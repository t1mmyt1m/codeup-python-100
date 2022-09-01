i, h, j = map(int, input().split())
print((i if i<h else h) if ((i if i<h else h)<j) else j)
