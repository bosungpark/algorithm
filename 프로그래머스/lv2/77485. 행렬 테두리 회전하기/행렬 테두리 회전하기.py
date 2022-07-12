def solution(rows, columns, queries):
    answer = []
    matrix=[[0 for _ in range(columns)] for _ in range(rows)]
    num=1
    for i in range(rows):
        for j in range(columns):
            matrix[i][j]+=num
            num+=1
    for q in queries:
        y1,x1,y2,x2=q[0],q[1],q[2],q[3]
        
        temp=[]
        for x in range(x1-1,x2-1):
            temp.append(matrix[y1-1][x])
        for y in range(y1-1,y2-1):
            temp.append(matrix[y][x2-1])
        for x in range(x2-1,x1-1,-1):
            temp.append(matrix[y2-1][x])
        for y in range(y2-1,y1-1,-1):
            temp.append(matrix[y][x1-1])  
        answer.append(min(temp))
        t=temp.pop()
        temp=[t]+temp
        for x in range(x1-1,x2-1):
            matrix[y1-1][x]=temp.pop(0)
        for y in range(y1-1,y2-1):
            matrix[y][x2-1]=temp.pop(0)
        for x in range(x2-1,x1-1,-1):
            matrix[y2-1][x]=temp.pop(0)
        for y in range(y2-1,y1-1,-1):
            matrix[y][x1-1]=temp.pop(0)
        # print(matrix)
        
    
    return answer