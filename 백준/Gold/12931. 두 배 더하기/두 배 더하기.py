N=int(input())
B=list(map(int, input().split()))

cnt=0
while B!=[0]*N:
    for i in range(N):
        # print(B)
        if B[i]%2:
            B[i]-=1
            cnt+=1
    if B!=[0]*N:
        for i in range(N):
            B[i]//=2
        # print(B)
        cnt+=1
print(cnt)