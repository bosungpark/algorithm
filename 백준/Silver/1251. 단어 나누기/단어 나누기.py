n=input()

array=[]
for i in range(1,len(n)):
    for j in range(i+1,len(n)):
        a,b,c=n[:i],n[i:j],n[j:]
        array.append(a[::-1]+b[::-1]+c[::-1])
print(sorted(array)[0])