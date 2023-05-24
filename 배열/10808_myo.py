#2023-05-23 PM 08:40

s = input()

a = 'abcdefghijklmnopqrstuvwxyz'
ar = [0]*len(a)
for i in s:
    ar[a.index(i)] += 1

print(*ar) #ar로 작성할 경우에는 답은 같지만 틀림(개별적인 인자로 전달안함)

#2023-05-23 PM 08:50