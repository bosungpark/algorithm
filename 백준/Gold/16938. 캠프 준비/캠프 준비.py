from itertools import combinations

n,l,r,x=map(int, input().split())
problems=sorted(list(map(int, input().split())))

cnt=0
for i in range(2,n+1):
    for c in combinations(problems,i):
        if l<=sum(c) and sum(c)<=r and c[-1]-c[0]>=x:
            cnt+=1 

print(cnt)