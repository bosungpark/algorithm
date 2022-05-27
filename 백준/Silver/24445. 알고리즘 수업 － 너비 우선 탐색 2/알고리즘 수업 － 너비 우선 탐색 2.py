import sys
from collections import defaultdict, deque

N,M,R=map(int, sys.stdin.readline().split())
graph=defaultdict(list)
for _ in range(M):
    u,v=map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

visited=dict()
stack=deque([R])
order=1
while stack:
    node=stack.popleft()
    if node not in visited:
        visited[node]=order
        order+=1
        stack.extend(sorted(graph[node], reverse=True))

for node in range(1,N+1):
    if node in visited:
        print(visited[node])
    else:
        print(0)