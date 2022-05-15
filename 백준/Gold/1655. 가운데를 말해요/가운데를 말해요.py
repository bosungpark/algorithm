import sys, heapq

N=int(sys.stdin.readline())

temp=int(sys.stdin.readline())
left=[(-temp,temp)]
right=[]

for _ in range(N-1):
    # print(left)
    # print(right)
    voice=int(sys.stdin.readline())
    middle=heapq.heappop(left)[1]
    print(middle)

    if voice<=middle:
        heapq.heappush(left,(-voice, voice))
    else:
        heapq.heappush(right,(voice, voice))
    
    heapq.heappush(right, (middle,middle))
    while len(left)<len(right):
        temp=heapq.heappop(right)[1]
        heapq.heappush(left, (-temp,temp))
print(heapq.heappop(left)[1])