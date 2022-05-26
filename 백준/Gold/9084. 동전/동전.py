import sys

T=int(sys.stdin.readline())

for _ in range(T):
    N=int(sys.stdin.readline())
    coins=list(map(int, sys.stdin.readline().split()))
    M=int(sys.stdin.readline())
    dp=[0 for _ in range(10001)]

    for coin in coins:
        dp[coin]+=1
        for i in range(1,10001):
            if i-coin>0:
                dp[i]+=dp[i-coin]
    print(dp[M])