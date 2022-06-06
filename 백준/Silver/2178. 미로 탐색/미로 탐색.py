N,M=map(int,input().split())
maze=list(list(map(int, list(input()))) for _ in range(N))

dx=[0,1,0,-1]
dy=[1,0,-1,0]
def bfs():
    queue=[[0,0]]
    
    while queue:
        node=queue.pop(0)
      
        for i in range(4):
            if 0<=node[0]+dx[i]<M and 0<=node[1]+dy[i]<N:
                if maze[node[1]+dy[i]][node[0]+dx[i]]==1:
                    queue.append([node[0]+dx[i],node[1]+dy[i]])
                    maze[node[1]+dy[i]][node[0]+dx[i]]=maze[node[1]][node[0]]+1
bfs()
print(maze[-1][-1])


