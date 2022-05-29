
import sys

M,N=map(int, sys.stdin.readline().split())
flag=list(list(map(int,sys.stdin.readline().split())) for _ in range(M))

dx=[0,1,0,-1,1,1,-1,-1]
dy=[-1,0,1,0,1,-1,1,-1]
def dfs(S):
    stack=[S]
    word=False
    while stack:    
        x,y=stack.pop()
        if flag[y][x]!=0:
            word=True
            flag[y][x]=0
            for i in range(8):
                if 0<=x+dx[i]<N and 0<=y+dy[i]<M:
                    stack.append((x+dx[i],y+dy[i]))
    return word
    
cnt=0
for y in range(M):
    for x in range(N):
        if dfs((x,y)):
            # for f in flag:
            #     print(f)
            # print()
            cnt+=1
print(cnt)