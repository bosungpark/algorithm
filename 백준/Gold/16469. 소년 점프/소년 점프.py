import sys
from collections import deque

R,C=map(int, sys.stdin.readline().split())
maze=list(list(sys.stdin.readline().strip()) for _ in range(R))
dx=[1,0,-1,0,0]
dy=[0,1,0,-1,0]
# print(maze)
def bfs(L):
    check=list(list(0 for _ in range(C)) for _ in range(R))
    queue=deque([L])
    while queue:
        x,y,depth=queue.popleft()
        # print(x,y)
        # if 0<=x<C and 0<=y<R:
        if maze[y][x]=='0' and not check[y][x]:
            check[y][x]+=depth
            for i in range(5):
                if 0<=x+dx[i]<C and 0<=y+dy[i]<R:
                    queue.append((x+dx[i],y+dy[i],depth+1))
    # print(check)
    return check

y,x=map(int, sys.stdin.readline().split())
# print()
nucksal=bfs((x-1,y-1,0))

y,x=map(int, sys.stdin.readline().split())
# print()
swings=bfs((x-1,y-1,0))

y,x=map(int, sys.stdin.readline().split())
# print()
changmo=bfs((x-1,y-1,0))

minimum=float("inf")
cnt=-1
for y in range(R):
    for x in range(C):
        if nucksal[y][x] and swings[y][x] and changmo[y][x]:
            if max(nucksal[y][x],swings[y][x],changmo[y][x])<minimum:
                minimum=max(nucksal[y][x],swings[y][x],changmo[y][x])
                cnt=1
            elif max(nucksal[y][x],swings[y][x],changmo[y][x])==minimum:
                cnt+=1
if minimum!=float("inf"):
    print(minimum)
print(cnt)


