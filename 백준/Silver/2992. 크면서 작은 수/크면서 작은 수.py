from itertools import permutations
import bisect

x=list(input())
array=sorted(set(''.join(p) for p in permutations(x,len(x))))
# print(array)
idx=bisect.bisect_right(array,''.join(x))
if idx<0 or idx>=len(array):
    print(0)
else:
    print(array[idx])