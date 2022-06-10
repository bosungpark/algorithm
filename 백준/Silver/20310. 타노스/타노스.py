S=list(input())

zero=0
one=0
for s in S:
    if s=='0':
        zero+=1
    elif s=='1':
        one+=1

for i in range(zero//2):
    for j in range(len(S)-1,-1,-1):
        if S[j]=='0':
            S[j]='*'
            break

for i in range(one//2):
    for j in range(len(S)-1):
        if S[j]=='1':
            S[j]='*'
            break

print("".join(S).replace("*",""))