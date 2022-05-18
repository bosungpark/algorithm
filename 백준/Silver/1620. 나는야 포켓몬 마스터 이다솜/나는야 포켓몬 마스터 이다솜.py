import sys

n,m=map(int,sys.stdin.readline().split())

id=dict()
name=dict()
for i in range(1,n+1):
    p=sys.stdin.readline().strip()
    id[i]=p
    name[p]=i

for _ in range(m):
    j=sys.stdin.readline().strip()
    try:
        j=int(j)
        print(id[j])
    except:
        print(name[j])