from collections import defaultdict, deque

n=int(input())

nodes=list(map(int, input().split()))
deleted_node=int(input())

gragh=defaultdict(list)
for idx, node in enumerate(nodes):
    gragh[node].append(idx)

def delete(graph, node):
    should_delete=gragh[node]
    gragh[node]=-2
    for s in should_delete:
        delete(graph, s)
delete(gragh, deleted_node)

q=deque([-1])
deleted_nodes=[deleted_node]
cnt=0
while q:
    node=q.popleft()   
    for next_node in gragh[node]:
        if gragh[next_node]==-2:
            continue
        if gragh[next_node]:
            for g in gragh[next_node]:
                if g==deleted_node and len(gragh[next_node])==1:
                    cnt+=1
            q.append(next_node)
        elif len(gragh[next_node])==0:
            cnt+=1
if gragh[deleted_node]==-1:
    print(0)
else:
    print(cnt)