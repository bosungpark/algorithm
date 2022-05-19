a,b,c=map(int, input().split())

def mul(a,b):  
    if b==0:
        return 1%c
    elif b==1:
        return a%c
    else:
        temp=mul(a,b//2)
        if b%2:
            return temp*temp*a%c
        else:
            return temp*temp%c

print(mul(a,b))