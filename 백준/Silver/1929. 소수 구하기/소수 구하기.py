M,N=map(int, input().split())
array=list(True for _ in range(N+1))

for i in range(2,N+1):
    if array[i]:
        for j in range(i*2, N+1, i):
            array[j]=False

for i in range(M,N+1):
    if array[i]:
        if i!=1:
            print(i)