T=int(input())

def prime_list(n):
    sieve = [True] * n

    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:   
            for j in range(i+i, n, i): 
                sieve[j] = False
    return [i for i in range(2, n) if sieve[i] == True]

def foo(K):
    p=prime_list(K)
    # print(p)
    for i in p:
        for j in p:
            for k in p:
                if i+j+k==K:
                    return print(i,j,k)
    return print(0)
                    

for _ in range(T):
    K=int(input())
    foo(K)



