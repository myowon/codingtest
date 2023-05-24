#2023-05-23 PM 09:15

N = list(str(input()))

set = [0]*10

for i in range(len(N)):
    a = int(N[i])
    if a == 6 or a == 9:
        if set[6] <= set[9]:
            set[6] += 1
        else:
            set[9] += 1
    else:
        set[a] += 1
        
print(max(set))

#2023-05-23 PM 09:35