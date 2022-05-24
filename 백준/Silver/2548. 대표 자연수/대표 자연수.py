n=int(input())
array=list(map(int, input().split()))

minimum=float("inf")
answer=-1
for i in range(n):
    temp=0
    for j in range(n):
        temp+=abs(array[i]-array[j])
    if minimum>temp:
        minimum=temp
        answer=array[i]
    if minimum==temp:
        answer=min(answer,array[i])
print(answer)