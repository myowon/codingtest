import sys

sen = str(sys.stdin.readline().strip())

a = sen.upper()
br = {}

for i in a:
    if i in br:
        br[i]+=1
    else:
        br[i]=1

max_value = max(br.values())
max_keys = [key for key, value in br.items() if value == max_value]

if len(max_keys)==1:
    print(max_keys[0])
else:
    print('?')
