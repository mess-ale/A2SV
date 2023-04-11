v = int(input())
for i in range(v):
    ad_matrix = list(map(int, input().split()))
    temp = []
    for i,val in enumerate(ad_matrix):
        if val == 1:
            temp.append(i+1)

    print(len(temp),*temp)
