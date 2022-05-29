import sys

R,C=map(int, sys.stdin.readline().split())
cage=list(list(sys.stdin.readline().strip()) for _ in range(R))

w=0
s=0

dx=[0,1,0,-1]
dy=[-1,0,1,0]
def dfs(S):
    global cage,w,s

    stack=[S]
    wolfs=0
    sheeps=0
    while stack:
        
        x,y=stack.pop()
        if cage[y][x]!="#":
            if cage[y][x]=="o":
                sheeps+=1
            if cage[y][x]=="v":
                wolfs+=1
            cage[y][x]="#"
            for i in range(4):
                if 0<=x+dx[i]<C and 0<=y+dy[i]<R:
                    stack.append((x+dx[i],y+dy[i]))
    if wolfs<sheeps:
        s+=sheeps
    else:
        w+=wolfs
for y in range(R):
    for x in range(C):
        dfs((x,y))
print(s,w)