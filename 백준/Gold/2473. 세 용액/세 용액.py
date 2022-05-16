n=int(input())
array=sorted(list(map(int, input().split())))
# print(sorted(array))

a,b,c=0,0,0
minimum=float("inf")
for i in range(n):
    start=i+1
    end=n-1
    while start<end:
        # print(i, start, end)
        # print(array[i]+array[start]+array[end],minimum)
        if abs(array[i]+array[start]+array[end])<minimum:
            minimum=abs(array[i]+array[start]+array[end])
            a,b,c=array[i],array[start],array[end]

        if array[i]+array[start]+array[end]==0:
            a,b,c=array[i],array[start],array[end]
            break
        elif array[i]+array[start]+array[end]<0:
            start+=1
        else:
            end-=1

print(a,b,c)

