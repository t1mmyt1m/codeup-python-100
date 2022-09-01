r, g, b = map(int, input().split())
num = 0

for i in range(0, r):
    for j in range(0, g):
        for h in range(0, b):
            print(i, j, h)
            
            num+=1
print(num)

