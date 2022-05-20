N,M=map(int, input().split())
A=set(map(int,input().split()))
B=set(map(int,input().split()))

C=A-B
if len(C)!=0:
    print(len(C))
    print(*sorted(C))
else:
    print(0)