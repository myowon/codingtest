##TIMEOVER##

# import sys

# zero = []
# one = []

# def fibonacci(n):
#     if (n == 0):
#         zero.append(1)
#         return 0
#     elif (n == 1):
#         one.append(1)
#         return 1
#     else:
#         return fibonacci(n-1) + fibonacci (n-2)
    
# T = int(sys.stdin.readline())

# for i in range(T):
#     n=int(input())
    
#     fibonacci(n)
    
#     print(len(zero), len(one))

import sys

def fibonacci(n):
    zero = 1
    one = 0
        
    for i in range(n):
        zero, one = one, zero + one # 피보나치수열 적용
    
    print(zero, one)
        
T = int(sys.stdin.readline())

for i in range(T):
    n = int(input())
    fibonacci(n)     
    