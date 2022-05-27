import sys
from collections import deque

n,m=map(int, sys.stdin.readline().split())
land=list(list(map(int, sys.stdin.readline().split())) for _ in range(n))
check=list(list("*" for _ in range(m)) for _ in range(n))

end=None
for i in range(n):
    for j in range(m):
        if land[i][j]==2:
            end=(i,j)
            break

dx=[1,0,-1,0]
dy=[0,1,0,-1]
check[end[0]][end[1]]=0
queue=deque([end])
while queue:
    node=queue.popleft()
    if land[node[0]][node[1]]!=-1:
        land[node[0]][node[1]]=-1

        for i in range(4):
            y=node[0]+dy[i]
            x=node[1]+dx[i]
            if 0<=y<n and 0<=x<m and land[y][x]!=0 and check[y][x]=="*":
                queue.append((y,x))
                check[y][x]=check[node[0]][node[1]]+1
            if 0<=y<n and 0<=x<m and land[y][x]==0 and check[y][x]=="*":
                check[y][x]=0
                
for i in range(n):
    for j in range(m):
        if check[i][j]!="*":
            print(check[i][j], end=" ")
        else:
            if land[i][j]==0:
                print(0, end=" ")
            else:
                print(-1, end=" ")
    print()