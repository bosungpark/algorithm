import sys

n=int(sys.stdin.readline())
graph=list(list(float("inf") for _ in range(n)) for _ in range(n))
check=list(list(0 for _ in range(n)) for _ in range(n))

for start in range(n):
    cities=list(map(int, sys.stdin.readline().split()))

    for end in range(n):
        graph[start][end]=cities[end]
def reverse_floyd_warshall():
    for middle in range(n):
        for start in range(n):
            for end in range(n):
                if middle==start or middle==end or start==end:
                    continue
                if graph[start][end]== graph[start][middle]+graph[middle][end]:
                    check[start][end]=1
                if graph[start][end]> graph[start][middle]+graph[middle][end]:
                    return print(-1)
    cost=0
    for row in range(n):
        for col in range(n):
            if not check[row][col]:
                cost+=graph[row][col]
    return print(cost//2)
reverse_floyd_warshall()