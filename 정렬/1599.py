import sys

n = int(sys.stdin.readline())

minSick = {"a":"A", "b":"B", "k":"C",
            "d": "D", "e":"E", "g":"F", 
            "h":"G", "i":"H", "l":"I",
            "m":"J", "n":"K",
            "o":"M", "p":"N", "r":"O",
            "s":"P", "t":"Q", "u":"R",
            "w":"S","y":"T"}
m = []

def change(c):
    re = c.replace('ng', 'L')
    for key, val in minSick.items():
        re = re.replace(key, val)
    return re
    
def dictionary(m):
    re = {}
    for i in m:
        temp = change(i)
        re[i] = temp
    re = sorted(re.items(), key=lambda x : x[0])
    #re = sorted(re, key=lambda x: re[x])
    return re

for i in range(n):
    m.append(input())

a = dictionary(m)

for i in range(n):
    print(a[i])
