import sys

n=int(sys.stdin.readline())
office=dict()
for _ in range(n):
    name,status=sys.stdin.readline().split()
    if status=="enter":
        office[name]=status
    else:
        office.pop(name,None)

for name in sorted(office,reverse=True):
    print(name)