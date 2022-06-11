M=int(input())
N=int(input())

primes=list(True for _ in range(N+1))

answers=[]
for i in range(2,N+1):
    if primes[i]:
        if i>=M:
            answers.append(i)
        for j in range(i*2,N+1,i):
            primes[j]=False

if answers:
    print(sum(answers))
    print(answers[0])
else:
    print(-1)