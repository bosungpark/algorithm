n=int(input())

square=list(list("*" for _ in range(n)) for _ in range(n))

def print_square(square):
    for s in square:
        print("".join(s))

def punch(row_start, col_start, total_line):
    for row in range(row_start+total_line//3,row_start+total_line//3*2):
        for col in range(col_start+total_line//3,col_start+total_line//3*2):
            square[row][col]=" "

while not n%3:
    for row_start in range(0,len(square),n):
        for col_start in range(0,len(square),n):
            punch(row_start, col_start, n)
    n//=3
print_square(square)