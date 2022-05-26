from itertools import permutations

N,M=map(int, input().split())
array=sorted(list(map(int, input().split())))

for p in permutations(array,M):
    print(*p)
