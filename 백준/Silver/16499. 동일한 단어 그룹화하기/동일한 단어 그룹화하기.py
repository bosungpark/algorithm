import sys

n=int(sys.stdin.readline())
words=set()
for _ in range(n):
    word=sys.stdin.readline()
    words.add("".join(sorted(word)))
print(len(words))