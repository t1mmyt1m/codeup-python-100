i, h, j = map(int, input().split())
#print(i+h+j, round((i+h+j)/3, 2))
#round를 쓰면 2.00이 아닌 2.0으로 출력되기 때문에 틀렸다 나옴.
print(i+h+j, format((i+h+j)/3, '.2f'))