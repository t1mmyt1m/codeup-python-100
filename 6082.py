i = int(input())
for h in range(1, i+1):
    if h%10==3 or h%10==6 or h%10==9:
        print("X", end=' ')
    else:
        print(h, end=' ')