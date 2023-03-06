n = int(input())
name_list = list(input().split())

n = int(input())
for i in range(n):
    new_commer = input()
    count = 0
    if "Bruk" in name_list:
        break 
    for j in range(len(name_list)):
        if ord(new_commer[0]) <= ord(name_list[j][0]):
            c = 1
            if ord(new_commer[0]) == ord(name_list[j][0]):
                while c < len(new_commer) and c < len(name_list) and ord(new_commer[c]) == ord(name_list[j][c]):
                    c += 1
                if ord(new_commer[c-1]) <= ord(name_list[j][c-1]):
                    print(j)
                    count += 1
                    name_list.pop()
                    break
            else:
                count += 1
                print(j)
                name_list.pop()
                break
    if count == 0:
        print(len(name_list))
