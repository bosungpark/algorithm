n,k=map(int, input().split())

idx=0
already_visited=[]
answer=False
def backTracking(visited):
    global idx, already_visited, answer
    # print(already_visited)

    if sum(visited)>n:
            return
    # print(visited)  
    for i in range(1,4):
        visited.append(i)   
        if sum(visited)==n and visited not in already_visited:
            idx+=1
            already_visited.append(visited.copy())
            # print(visited,idx)
            if idx==k:           
                answer= visited.copy()
                return
        backTracking(visited)
        visited.pop()
    return


backTracking([])
if answer:
    print(*answer, sep="+")
else:
    print(-1)

