from itertools import combinations

N,M=map(int, input().split())
array=sorted(list(map(int, input().split())))

for c in combinations(array, M):
    print(*c)