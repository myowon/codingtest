#시간초과
# import sys

# s= list(str(sys.stdin.readline()))
# s.pop(-1)

# m = int(sys.stdin.readline())
# cursor = len(s)

# for i in range(m):
#     a = sys.stdin.readline().split()
    
#     if a[0] == 'L' and cursor > 0:
#         cursor -= 1
#     elif a[0] == 'D' and cursor <len(s):
#         cursor += 1
#     elif a[0] == 'B' and cursor > 0:
#         s.pop(cursor-1)
#         cursor -= 1
#     elif a[0] == 'P':
#         s.insert(cursor, a[1])
#         cursor += 1

# print("".join(s))

import sys

s= list(str(sys.stdin.readline()))
s.pop(-1)

r = []
m = int(sys.stdin.readline())

for i in range(m):
    a = sys.stdin.readline().split()
    
    if a[0] == 'L' and s:
        r.append(s.pop())
    elif a[0] == 'D' and r:
        s.append(r.pop())
    elif a[0] == 'B' and s:
        s.pop()
    elif a[0] == 'P':
        s.append(a[1])

result = s + r[::-1]

print("".join(result))