# 시간 초과
# import sys
# from collections import deque

# T = int(sys.stdin.readline())

# for _ in range(T):
#     P = list(str(sys.stdin.readline().strip()))
#     n = int(sys.stdin.readline())
#     arr = sys.stdin.readline().strip()[1:-1].split(',')
#     ar = deque()
    
#     for e in arr:
#         if e:
#             ar.append(int(e))
            
#     for i in P:
#         if i == 'R':
#             ar.reverse()
#         elif i == 'D':
#             if len(ar) == 0:
#                 break
#             else:
#                 ar.popleft()
#     if len(ar) == 0:
#         print('error')
#     else:
#         print(list(ar))


import sys
from collections import deque

T = int(sys.stdin.readline())

for _ in range(T):
    P = list(str(sys.stdin.readline().strip()))
    n = int(sys.stdin.readline())
    ar = deque(sys.stdin.readline().strip()[1:-1].split(','))

    if '' in ar:
        ar.remove('')
    
    reverse_flag = False
    error_flag = False
    
    for i in P:
        if i == 'R':
            reverse_flag = not reverse_flag
        elif i == 'D':
            if len(ar) == 0:
                error_flag = True
                break
            if reverse_flag:
                ar.pop()
            else:
                ar.popleft()
                
    if error_flag:
        print('error')
    else:
        if reverse_flag:
            ar.reverse()
        print('['+','.join(ar)+']')
