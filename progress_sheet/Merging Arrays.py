lis = list(map(int, input().split()))
array1 = list(map(int, input().split()))
array2 = list(map(int, input().split()))
result = []
i = 0
j = 0
while True:
    if i > len(array1)-1 or j > len(array2)-1:
        break
    elif array1[i] < array2[j]:
        result.append(array1[i])
        i += 1
    else:
        result.append(array2[j])
        j += 1

result.extend(array1[i:])
result.extend(array2[j:])
for i in range(len(result)):
    print(result[i], end=" ")