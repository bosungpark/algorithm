import sys

sys.setrecursionlimit(1000)

N,M=map(int, input().split())
array=sorted(list(map(int, input().split())))

def dfs(stack, visited, idx):
    if len(stack)==M:
        stack=sorted(stack)
        if stack not in visited:
            visited.append(stack)
            return print(*stack)
        return      
    for i in range(idx,N):
        stack.append(array[i])
        dfs(stack=stack, visited=visited, idx=i)
        stack.pop()

dfs(stack=[], visited=[],idx=0)