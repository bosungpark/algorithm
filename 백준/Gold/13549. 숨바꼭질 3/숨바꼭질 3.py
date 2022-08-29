import heapq

n,k=map(int, input().split())

stack=[[0,n]]
heapq.heapify(stack)
costs=[float("inf") for _ in range(100001)]
costs[n]=0

while stack:    
    node=heapq.heappop(stack)
    if costs[node[1]]<node[0]:
            continue 
    for next_node in [[node[0]+1,node[1]+1],[node[0]+1,node[1]-1],[node[0],node[1]*2]]:
        node=next_node[1]
        cost=next_node[0]
        if 0<=node<100001 and cost<costs[node]:
            costs[node]=cost
            heapq.heappush(stack,[cost,node])
print(costs[k])