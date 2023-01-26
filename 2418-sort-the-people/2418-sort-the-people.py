lis = list(map(int, input().split()))
array2 = list(map(int, input().split()))
array1 = list(map(int, input().split()))


result = []
i = 0
j = 0
count = 0
while i <= len(array1)-1:
    if j > len(array2)-1:
        i += 1
        result.append(count)
    elif array1[i] > array2[j]:
        count += 1
        j += 1
    else:
        i += 1
        result.append(count)
        
for i in range(0, len(result)):
    print(result[i], end=" ")
    
    
    