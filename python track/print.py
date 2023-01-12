# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
s = []
for i in range(0,n):
    r = input()
    s.append(r)

ins = []
num = 0
for i in range(0, len(s)):
    count = 1
    for j in range(i + 1, len(s)):
        if s[i] == s[j]:
            count += 1
            num = j
    ins.append(count)
ins.remove(ins[num])
print(len(ins))
print(*ins)
