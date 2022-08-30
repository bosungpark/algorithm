import sys

v,e=map(int, sys.stdin.readline().split())

graph=list(list(float("inf") for _ in range(v)) for _ in range(v))
for _ in range(e):
    a,b,c=map(int, sys.stdin.readline().split())
    graph[a-1][b-1]=c

def floyd_warshall():
    for middle in range(v):
        for start in range(v):
            for end in range(v):
                if graph[start][end]>graph[start][middle]+graph[middle][end]:
                    graph[start][end]=graph[start][middle]+graph[middle][end]
    cost=float("inf")
    for start in range(v):
        for end in range(v):
            cost=min(cost, graph[start][end]+graph[end][start])
    if cost==float("inf"):
        cost=-1
    return cost

print(floyd_warshall())