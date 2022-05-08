""" 
저는 이 문제를 a와 b만 구해주면 된다는 접근으로 해결하였습니다. 

우선 이중 for 문을 사용해 a,b를 구해주었습니다. 
이때 두번째 for 문은 첫번째 for 문의 인덱스 다음 번 부터 출력해줍니다.
반복이 모두 완료된 시점에서 두번쩨 for문의 절반 가량은 탐색이 되지 않았습니다. 
따라서 반복문에서의 시간 복잡도는 O(nlogn)이라도 생각합니다. 

다음은 마지막 요소 c를 구하는 과정입니다. 
c는 a와 b가 구해졌기 때문에 특정이 가능합니다. 
따라서 c의 범위를 array 배열에서 이분탐색 해주었습니다.
이 과정의 시간 복잡도는 로그 시간 복잡도를 가집니다. 

최종적으로 이분탐색을 통해 찾은 c의 갯수를 cnt에 더해 출력해줍니다. 
전체 시간 복잡도는 O(nlogn*logn)입니다. 
""" 
import sys
from collections import deque
from bisect import bisect_left, bisect_right 

n=int(sys.stdin.readline())
array=list(int(sys.stdin.readline()) for _ in range(n)) 
array.sort() 

cnt=0 
for a in range(n): 
  for b in range(a+1,n): 
    c_left= bisect_left(array, 2*array[b]-array[a])
    c_right= bisect_right(array, 2*(array[b]-array[a])+array[b])
    
    if c_right-c_left>0: 
      cnt+=c_right-c_left 
      
print(cnt)
