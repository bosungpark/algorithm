from itertools import combinations

t=int(input())

def gcb(a,b):
    if a<b:
        a,b=b,a

    while b:
        a,b=b,a%b
    return abs(a)

for _ in range(t):
    n,*array=map(int, input().split())

    sum=0
    for c in combinations(array,2):
        sum+=gcb(c[0],c[1])
    print(sum)