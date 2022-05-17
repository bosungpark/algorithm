import sys, heapq

T=int(sys.stdin.readline())

for _ in range(T):
    middles=[]
    i=0
    left=[]
    right=[]
    M=int(sys.stdin.readline())
    for _ in range(M//10+1):
        array=list(map(int, sys.stdin.readline().split()))

        
        if not left:
            left.append(-array[0])
        for m in array:
            middle=-heapq.heappop(left)
            if m>=middle:
                heapq.heappush(right,m)
            else:
                heapq.heappush(left,-m)
            if i!=0:
                heapq.heappush(right,middle)

            while len(right)>=len(left):
                m=heapq.heappop(right)
                heapq.heappush(left,-m)
            
            if not i%2:
                m=-heapq.heappop(left)
                middles.append(m)
                heapq.heappush(left,-m)
            i+=1

    print(len(middles))
    for i,m in enumerate(middles):
        print(m, end=" ")
        if i%10==9:
            print()
    print()
