# Enter your code here. Read input from STDIN. Print output to STDOUT
k1 = int(input())
A = list(map(int, input().split()))
k2 = int(input())
B = list(map(int, input().split()))

count = 0
for i in A:
    if i in B:
        count += 1
        
print(len(A)-count)
