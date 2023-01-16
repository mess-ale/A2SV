# Enter your code here. Read input from STDIN. Print output to STDOUT
given_superset = list(map(int, input().split()))
k = int(input())
ls = []
for i in range(k):
    ask_set1 = list(map(int, input().split()))
    ls.append(ask_set1)
    
s = True
for j in range(0, len(ls)):
    for k in range(0, len(ls[j])):
        if ls[j][k] in given_superset:
            continue
        else:
            s = False
            print(s)
            break
    if s == False:
        break
if s:
    print(True)
    
