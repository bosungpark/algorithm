n,k=map(int, input().split())
array=sorted(list(map(int, input().split())), reverse=True)

print(array[k-1])