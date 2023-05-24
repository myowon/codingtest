A = int(input())
B = int(input())
C = int(input())

re = list(str(A*B*C))

for i in range(10):
    print(re.count(str(i)))