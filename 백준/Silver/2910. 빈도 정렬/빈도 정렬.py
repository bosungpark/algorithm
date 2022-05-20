N,C=map(int, input().split())
array=list(map(int,input().split()))

count=dict()
for i,a in enumerate(array):
    if a in count:
        count[a][0]+=1
    else:
        count[a]=[1,i]

for key, value in sorted(count.items(), key=lambda x: (-x[1][0],x[1][1])):
    for _ in range(value[0]):
        print(key, end=" ")

    