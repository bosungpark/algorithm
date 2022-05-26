N,M=map(int, input().split())
array=sorted(list(map(int, input().split())))

visited=[]
def dfs(stack,idx):
    global visited

    if len(stack)==M:
        if stack not in visited:
            visited.append(stack.copy())
            print(*stack)
        return
    for i in range(idx,N):
        stack.append(array[i])
        idx=i
        dfs(stack,idx)
        stack.pop()
dfs([],0)