N=int(input())

start=0
end=N
while start<end:
    mid=(start+end)//2
    if mid**2==N:
        print(mid)
        break
    elif mid**2<N:
        start=mid
    else:
        end=mid