n=int(input())

i=2
while n!=1:
    if n%i:
        i+=1
    else:
        print(i)
        n//=i
