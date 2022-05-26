from itertools import permutations

N,M=map(int, input().split())
array=sorted(list(map(int, input().split())))

visited=[]
for p in permutations(array, M):
    p=sorted(p)
    if p not in visited:
        visited.append(p)
        print(*p)