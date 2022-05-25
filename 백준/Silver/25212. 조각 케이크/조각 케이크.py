from itertools import combinations

n=int(input())

def foo(n):
    if n!=0:
        return 1/int(n)
    else:
        return 0

array=list(map(foo, input().split()))
# print(array)
cnt=0
for i in range(1,n+1):
    comb=combinations(array,i)
    for c in comb:
        if 99/100<=sum(c)<=101/100:
            cnt+=1
print(cnt)