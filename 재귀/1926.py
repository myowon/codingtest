import sys
sys.setrecursionlimit(10**6)

a, b, c = map(int, sys.stdin.readline().split())

# 지수 법칙 : A^(m+n) = A^m x A^n
# 나머지 분배 법칙 : (AxB)%C = (A%C) *(B%C) % C
# 10^11 % 12
# = ((10^5)%12 x (10^5)%12 x 10)% 12
# = ((10^2)%12 x (10^2)%12 x 10) %12 x (10^2)%12 x (10^2)%12 x 10) %12 x 10) %12

def mul(x, y, z):
    if y == 0:
        return 1
    elif y == 1:
        return x % z
    else:
        h = mul(x, y//2, z)
        if y % 2 == 0:
            return (h*h)%z
        else:
            return (h*h*x)%z

print(mul(a,b,c))