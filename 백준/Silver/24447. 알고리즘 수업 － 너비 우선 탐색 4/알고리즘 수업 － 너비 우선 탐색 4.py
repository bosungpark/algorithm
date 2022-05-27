import sys
from collections import defaultdict, deque

N,M,R=map(int, sys.stdin.readline().split())
graph=defaultdict(list)
for _ in range(M):
    u,v=map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

visited=dict()
order=1
stack=deque([(R,0)])
while stack:
    node,depth=stack.popleft()
    if node not in visited:
        visited[node]=(depth,order)
        order+=1
        for n in sorted(graph[node]):
            stack.append((n,depth+1))

sum=0
for d,o in visited.values():
    sum+=d*o
print(sum)