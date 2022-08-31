import sys

n,m=map(int, sys.stdin.readline().split())
parents=dict()
for i in range(n):
    parents[i]=i

def find(x):
    if x!=parents[x]:
        return find(parents[x])
    else:
        return parents[x]

def union(x,y):
    x=find(x)
    y=find(y)

    if x<y:
        parents[y]=x
    else:
        parents[x]=y

def solver():
    for idx in range(m):
        a,b=map(int, sys.stdin.readline().split())
        if find(a)==find(b):
            return print(idx+1)
        union(a,b)
    return print(0)
solver()