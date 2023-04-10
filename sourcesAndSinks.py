def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s) - 1]))
def invr():
    return(map(int,input().split()))

n = inp()
adjacentmatrix = []
for i in range(n):
    ls = inlt()
    adjacentmatrix.append(ls)

source = []
for i,val in enumerate(adjacentmatrix):
    if len(set(val)) == 1 and val[0] == 0:
        source.append(i+1)

sink = []
num_rows = len(adjacentmatrix)
num_cols = len(adjacentmatrix[0])
new_matrix = [[0 for j in range(num_rows)] for i in range(num_cols)]
for i in range(num_rows):
    for j in range(num_cols):
        new_matrix[j][i] = adjacentmatrix[i][j]

for i,val in enumerate(new_matrix):
    if len(set(val)) == 1 and val[0] == 0:
        sink.append(i+1)
        
print(len(sink), *sink)
print(len(source),*source)
