import sys

N, K = map(int, sys.stdin.readline().split())

ar = []
for i in range(N):
    W, V = map(int, sys.stdin.readline().split())
    ar.append([W,V])
    
dp = [0 for _ in range(K+1)]

for a in ar:
    W, V = a
    for i in range(K, W-1, -1):
        dp[i] =  max(dp[i], dp[i-W]+V)
        
print(dp[K])