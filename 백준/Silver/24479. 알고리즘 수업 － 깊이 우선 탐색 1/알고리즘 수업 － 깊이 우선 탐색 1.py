import sys
from collections import defaultdict

N,M,R=map(int, sys.stdin.readline().split())
graph=defaultdict(list)

for _ in range(M):
    u,v=map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

def dfs():
    visited=dict()
    stack=[R]

    idx=1
    while stack:
        node=stack.pop()
        if node not in visited:
            visited[node]=idx
            idx+=1
            stack.extend(sorted(graph[node],reverse=True))
    return visited

visited=dfs()
for i in range(1,N+1):
    if i in visited:
        print(visited[i])
    else:
        print(0)