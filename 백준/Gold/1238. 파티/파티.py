from collections import defaultdict
import heapq

n,m,x=map(int, input().split())

graph=defaultdict(list)
for _ in range(m):
    s,e,t=map(int, input().split())
    graph[s].append([t,e])

max_time=0
for i in range(1,n+1):
    q=[[0,i]]
    dist=[float('inf') for __ in range(n+1)]
    temp=0

    while q:
        time,start=heapq.heappop(q)
        if dist[start]<time:
            continue

        dist[start]=min(dist[start],time)

        for node in graph[start]:
            cost=time+node[0]
            if dist[node[1]]>cost:
                dist[node[1]]=cost
                heapq.heappush(q,[(cost),node[1]])
    temp+=dist[x]

    q=[[0,x]]
    dist=[float('inf') for __ in range(n+1)]

    while q:
        time,start=heapq.heappop(q)
        if dist[start]<time:
            continue

        for node in graph[start]:
            cost=time+node[0]
            if dist[node[1]]>cost:
                dist[node[1]]=cost
                heapq.heappush(q,[(cost),node[1]])
    temp+=dist[i]

    max_time=max(max_time,temp)

print(max_time)