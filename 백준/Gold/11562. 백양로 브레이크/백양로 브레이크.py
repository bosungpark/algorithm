import sys

n,m=map(int, sys.stdin.readline().split())
graph=list(list(float("inf") for _ in range(n)) for _ in range(n))

for _ in range(m):
    u,v,b=map(int, sys.stdin.readline().split())
    graph[u-1][v-1]=0
    if b:
        graph[v-1][u-1]=0
    else:
        graph[v-1][u-1]=1

for i in range(n):
    graph[i][i]=0

def floyd_warshall():
    for middle in range(n):
        for start in range(n):
            for end in range(n):
                if graph[start][end]>graph[start][middle]+graph[middle][end]:
                    graph[start][end]=graph[start][middle]+graph[middle][end]
floyd_warshall()
k=int(sys.stdin.readline())
for _ in range(k):
    s,e=map(int, sys.stdin.readline().split())      
    print(graph[s-1][e-1])