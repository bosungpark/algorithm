N,M=map(int, input().split())
electronics=sorted(list(map(int, input().split())))

sockets=list(0 for _ in range(M))
for i in range(M):
    if electronics:
        sockets[i]+=electronics.pop()

cnt=0
while True:
    cnt+=1
    for i in range(M):
        if sockets[i]: 
            sockets[i]-=1
        if not sockets[i]:
            if electronics:
                sockets[i]+=electronics.pop()
            else:
                pass

    if sockets==[0 for _ in range(M)]:
        break
print(cnt)