import sys


N=int(sys.stdin.readline())
array=sorted(list(int(sys.stdin.readline()) for _ in range(N)))

for a in array:
    print(a)