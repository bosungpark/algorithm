from itertools import permutations

def is_prime(n):
    if n==1 or n==0:
        return False
    for i in range(2, n):
    	if n % i == 0:		
        	return False
    return True			
    

def solution(numbers):
    answer = 0
    temp=set()
    
    for j in range(1,len(numbers)+1):
        for i in set(int("".join(p)) for p in permutations(numbers,j)):
            temp.add(i)
    print(temp)
    for t in temp:
        if is_prime(t):
            answer+=1         
    return answer