from itertools import product

T=int(input())

for _ in range(T):
    N=int(input())
    array=list(str(a) for a in range(1,N+1))
    signs=product([' ','+','-'],repeat=N-1)
    for s in signs:
        temp=array[0]
        for i in range(N-1):
            temp+=s[i]+array[i+1]
        if eval(temp.replace(' ',''))==0:
            print(temp)
    print()