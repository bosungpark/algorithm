import sys

T=int(sys.stdin.readline())

dx=[0,1,0,-1]
dy=[-1,0,1,0]
def dfs(S):
    sheep=False
    stack=[S]
    while stack:    
        x,y=stack.pop()
        if field[y][x]!=".":
            sheep=True
            field[y][x]="."
            for i in range(4):
                if 0<=x+dx[i]<W and 0<=y+dy[i]<H:
                    stack.append((x+dx[i],y+dy[i]))
    return sheep

for _ in range(T):
    H,W=map(int, sys.stdin.readline().split())
    field=list(list(sys.stdin.readline()) for _ in range(H))

    cnt=0
    for y in range(H):
        for x in range(W):
            if dfs((x,y)):
                cnt+=1
    print(cnt)