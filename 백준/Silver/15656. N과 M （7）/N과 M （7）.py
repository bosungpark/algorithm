from itertools import product

N,M=map(int, input().split())
array=sorted(list(map(int, input().split())))

for p in product(array, repeat=M):
    print(*p)