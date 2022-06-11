N=int(input())

def is_prime(n):
    if n==0:
        return
    if n==1:
        return
    for i in range(2,n):
        if not n%i:
            return False
    return True

visited=[]
def dfs():
    if 0<len(visited)<N:
        n=int(''.join(visited).lstrip())
        if not is_prime(n):
            return
    if len(visited)==N:
        n=''.join(visited)
        if is_prime(int(n)):
            print(n)
        return
    for i in range(10):
        visited.append(str(i))
        dfs()
        visited.pop()
dfs()