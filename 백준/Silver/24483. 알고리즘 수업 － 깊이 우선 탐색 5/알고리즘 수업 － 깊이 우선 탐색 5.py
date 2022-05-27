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
order=1
while stack:
    node, depth=stack.pop()
    if node not in tree:
        tree[node]=(depth,order)
        order+=1
        for n in sorted(graph[node],reverse=True):
            stack.append((n,depth+1))
sum=0
for depth, order in tree.values():
    sum+=depth*order
print(sum)