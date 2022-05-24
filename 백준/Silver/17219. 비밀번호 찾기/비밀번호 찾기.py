import sys

N,M=map(int,sys.stdin.readline().split())
info=dict()
for _ in range(N):
    site,pw=sys.stdin.readline().strip().split()
    info[site]=pw

for _ in range(M):
    site=sys.stdin.readline().strip()
    print(info[site])