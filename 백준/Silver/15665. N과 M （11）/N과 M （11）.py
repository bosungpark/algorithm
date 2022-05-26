N,M=map(int, input().split())
array=sorted(set(map(int, input().split())))

def dfs(stack):
    global visited

    if len(stack)==M:
        print(*stack)
        return
    for i in range(len(array)):
        stack.append(array[i])
        dfs(stack)
        stack.pop()
dfs([])