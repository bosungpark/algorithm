import sys
from collections import defaultdict

n,m=map(int, sys.stdin.readline().split())

graph=defaultdict(list)
for _ in range(m):
    a,b,c=map(int, sys.stdin.readline().split())
    graph[a].append([b,c])
    graph[b].append([a,c])

s,t=map(int, sys.stdin.readline().split())

stack=[[s,0]]
costs=[float("inf") for _ in range(n+1)]
costs[s]=0

while stack:
    node=stack.pop()
    if costs[node[0]]<node[1]:
            continue 
   
    for next_node in graph[node[0]]:
        cost=node[1]+next_node[1]
        if cost<costs[next_node[0]]:
            costs[next_node[0]]=cost
            stack.append([next_node[0],cost]) 
print(costs[t])  