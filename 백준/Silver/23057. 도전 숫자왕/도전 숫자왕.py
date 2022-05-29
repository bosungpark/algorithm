from itertools import combinations

n=int(input())
array=list(map(int, input().split()))

sum_list=set()
for i in range(1,n+1):
    for comb in combinations(array,i):
        sum_list.add(sum(comb))

print(sum(array)-len(sum_list))
