n=int(input())

dp_cnt=0
def dp(n):
    global dp_cnt

    fibo=[0 for _ in range(n+1)]
    fibo[1]=1
    fibo[2]=1
    for i in range(3,n+1):
        dp_cnt+=1
        fibo[i]=fibo[i-1]+fibo[i-2]
    return fibo[-1]

recursion_cnt=0
def recursion(n):
    global recursion_cnt
    
    if n==1 or n==2:
        recursion_cnt+=1
        return 1
    else:
        return recursion(n-1)+recursion(n-2)

dp(n)
recursion(n)

print(recursion_cnt, dp_cnt)