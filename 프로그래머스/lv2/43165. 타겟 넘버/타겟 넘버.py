def solution(numbers, target):
    answer = 0
    
    def dfs(visited):
        nonlocal answer
        
        if len(visited)==len(numbers):
            temp=0
            for j in range(len(numbers)):
                if visited[j]=="+":
                    temp+=numbers[j]
                else:
                    temp-=numbers[j]
            if temp==target:
                answer+=1
            return
        
        for o in ("+","-"):
            visited.append(o)
            dfs(visited)
            visited.pop()
    dfs([])
        
    return answer