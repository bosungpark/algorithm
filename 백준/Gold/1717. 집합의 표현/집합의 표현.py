n,m=map(int, input().split())
parents=[i for i in range(n+1)]

def find(x):
    if parents[x]!=x:
        return find(parents[x])
    return x

def union(x,y):
    x=find(x)
    y=find(y)
    
    if x>y:
        parents[y]=x
    else:
        parents[x]=y

for _ in range(m):
    o,a,b=map(int, input().split())
    if not o:
        union(a,b)
    else:
        if find(a)==find(b):
            print("YES")
        else:
            print("NO")