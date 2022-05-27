import sys
from collections import defaultdict

N,M,R=map(int, sys.stdin.readline().split())
graph=defaultdict(list)
tree=dict()
for _ in range(M):
    u,v=map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)


stack=[(R,0)]
while stack:
    node, depth=stack.pop()
    if node not in tree:
        tree[node]=depth

        for n in sorted(graph[node],reverse=False):
            stack.append((n,depth+1))

for i in range(1,N+1):
    if i in tree:
        print(tree[i])
    else:
        print(-1)