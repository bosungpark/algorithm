from itertools import permutations

array=sorted(list(input()), reverse=True)


def foo():
    temp=int(''.join(array).lstrip("0"))
    if not temp%30:
        return print(temp)
    return print(-1)
foo()