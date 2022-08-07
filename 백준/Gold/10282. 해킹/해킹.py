from collections import defaultdict
import heapq

t= int(input())
for _ in range(t):
    n,d,c=map(int, input().split())
    graph=defaultdict(list)

    for _ in range(d):
        a,b,s=map(int, input().split())
        graph[b].append([s,a])

    q=[[0,c]]
    dist=[float('inf') for _ in range(n+1)]
    while q:
        time, computer=heapq.heappop(q)
        
        if time>dist[computer]:
            continue
        dist[computer]=min(dist[computer],time)

        for comp in graph[computer]:
            cost=comp[0]+time
            if cost<dist[comp[1]]:
                dist[comp[1]]=cost
                heapq.heappush(q,[cost,comp[1]])
    number=0
    max_num=0
    for i in dist:
        if i!=float('inf'):
            number+=1
            max_num=max(max_num,i)
    print(number,max_num)