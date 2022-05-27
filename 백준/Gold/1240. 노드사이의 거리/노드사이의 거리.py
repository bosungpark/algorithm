import sys
from collections import defaultdict

N,M=map(int, sys.stdin.readline().split())
dp=list(list(float("inf") for _ in range(N+1)) for _ in range(N+1))
graph=defaultdict(list)

for _ in range(N-1):
    u,v,c=map(int, sys.stdin.readline().split())
    dp[u][v]=c
    dp[v][u]=c

    graph[u].append(v)
    graph[v].append(u)

for _ in range(M):
    u,v=map(int, sys.stdin.readline().split())
    # print(dp[u][v])

    stack=[(u,0)]
    visited=[]
    while stack:
        node,cost=stack.pop()
        # print(node,cost)
        if node==v:
            dp[u][v]=min(dp[u][v],cost)
            dp[v][u]=min(dp[u][v],cost)
            continue
        if node not in visited:
            visited.append(node)
            for n in graph[node]:
                stack.append((n,cost+dp[node][n]))
    print(dp[u][v])