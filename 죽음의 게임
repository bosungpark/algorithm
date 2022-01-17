import sys

N,K=map(int,sys.stdin.readline().split())

round=list(int(sys.stdin.readline()) for _ in range(N))

def The_game_of_death(K):
    M=0
    queue=[0]
    visited=[]
    while queue:        
        now=queue.pop()
        visited.append(now)
        if round[now] not in visited:
            queue.append(round[now])       
        if now==K:
            return print(M)
        M+=1
            
    return print(-1)

The_game_of_death(K)
