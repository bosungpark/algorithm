n=int(input())
array=list(map(int, input().split()))

def is_prime(num):
    for i in range(2,num):
        if not num%i:
            return False
    return True

cnt=0
for a in array:
    if is_prime(a) and a!=1:
        cnt+=1
print(cnt)