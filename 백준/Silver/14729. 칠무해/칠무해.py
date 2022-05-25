import heapq, sys

n=int(sys.stdin.readline())
q=[]
for _ in range(n):
    score=float(sys.stdin.readline())
    heapq.heappush(q,score)

for _ in range(7):
    print("{0:0.3f}".format(heapq.heappop(q)))

