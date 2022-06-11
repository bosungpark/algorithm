import sys
from itertools import permutations

T=int(sys.stdin.readline())
for _ in range(T):
    k=int(sys.stdin.readline())
    array=list(sys.stdin.readline().strip() for _ in range(k))

    answers=[]
    permutation=permutations(array,2)
    for p in permutation:
        s=''.join(p)
        if s==s[::-1]:
            answers.append(s)
            break
    if answers:
        print(*answers)
    else:
        print(0)