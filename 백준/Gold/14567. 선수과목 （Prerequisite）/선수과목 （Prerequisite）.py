import sys
from collections import defaultdict

N,M=map(int, sys.stdin.readline().split())
graph=defaultdict(list)
answer=[0 for _ in range(N+1)]

for _ in range(M):
    before, after=map(int, sys.stdin.readline().split())
    graph[after].append(before)

depths=dict()
for start in range(1,N+1):

    stack=[(start,1)]
    visited=[]
    maximum_depth=0
    temp_depths=dict()
    while stack:
        node,depth=stack.pop()
        if node in depths:
            # print(depth,maximum_depth,depths[node])
            maximum_depth=max(maximum_depth, depth-1+depths[node])
            continue
        if node not in visited:
            visited.append(node)
            if depth>maximum_depth:
                maximum_depth=depth
            temp_depths[node]=depth
            for n in graph[node]:
                stack.append((n,depth+1))

    for n, d in temp_depths.items():
        if n not in depths:
            depths[n]=maximum_depth-d+1
    print(maximum_depth, end=" ")
    # print(depths)