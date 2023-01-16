# Enter your code here. Read input from STDIN. Print output to STDOUT
k1 = int(input())
A = list(map(int, input().split()))
k2 = int(input())
B = list(map(int, input().split()))

result = len(A) + len(B)
for i in A:
    if i in B:
        result -= 1

print(result)
