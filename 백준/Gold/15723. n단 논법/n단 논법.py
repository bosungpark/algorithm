import sys
from collections import defaultdict

n=int(sys.stdin.readline())
graph=defaultdict(list)
for _ in range(n):
    u,v=sys.stdin.readline().split(" is ")
    graph[u.strip()].append(v.strip())

def dfs(u,v):
    stack=[u]
    visited=[]
    while stack:
        node=stack.pop()
        # print(node, v)
        if node==v:
            return print("T")
            
        if node not in visited:
            visited.append(node)
            stack.extend(graph[node])
    return print("F")

m=int(sys.stdin.readline())
for _ in range(m):
    u,v=sys.stdin.readline().split(" is ")
    dfs(u.strip(),v.strip())