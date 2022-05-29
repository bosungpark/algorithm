import sys

N,M=map(int, sys.stdin.readline().split())

campus=list(list(sys.stdin.readline().strip()) for _ in range(N))
dx=[1,0,-1,0]
dy=[0,1,0,-1]
cnt=0
def dfs(S):
    global cnt

    stack=[S]
    while stack:
        x,y=stack.pop()
        if campus[y][x]=="P":
            cnt+=1
        if campus[y][x]!="X":
            campus[y][x]="X"
            for i in range(4):
                if 0<=x+dx[i]<M and 0<=y+dy[i]<N:
                    stack.append((x+dx[i],y+dy[i]))
for i in range(N):
    for j in range(M):
        if campus[i][j]=="I":
            dfs((j,i))
            # for c in campus:
            #     print(c)
            break
if cnt:
    print(cnt)
else:
    print("TT")