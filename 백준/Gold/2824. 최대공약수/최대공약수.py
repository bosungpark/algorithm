from functools import reduce
from math import gcd

N=int(input())
ns=list(map(int, input().split()))

M=int(input())
ms=list(map(int, input().split()))

n=reduce(lambda x, y: x * y, ns)
m=reduce(lambda x, y: x * y, ms)
answer=gcd(n,m)
print(str(answer)[-9:])