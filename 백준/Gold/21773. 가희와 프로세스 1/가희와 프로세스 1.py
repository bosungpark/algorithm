import sys, heapq


T, n=map(int,sys.stdin.readline().split())

q=[]
for _ in range(n):
    p_id, t, p=map(int,sys.stdin.readline().split())
    heapq.heappush(q,[-p,p_id,t])

while T:
    temp=heapq.heappop(q)
    temp[0]+=1
    temp[2]-=1
    
    if temp[2] >= 0:
        heapq.heappush(q,temp)
        print(temp[1])
        T-=1

    if not q:
        break