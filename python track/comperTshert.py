x = int(input())
dic = {"S":1, "M":2, "L":3}
for i in range(x):
    lsi = list(input().split())
    
    if dic[lsi[0][-1]] >  dic[lsi[1][-1]]:
        print(">")
    
    elif dic[lsi[0][-1]] <  dic[lsi[1][-1]]:
        print("<")
    
    elif dic[lsi[0][-1]] ==  dic[lsi[1][-1]]:
        if lsi[0][-1] == "S":
            if len(lsi[0]) > len(lsi[1]):
                print("<")
            elif len(lsi[0]) < len(lsi[1]):
                print(">")
            else:
                print("=")  
                
        elif len(lsi[0]) > len(lsi[1]):
            print(">")
        elif len(lsi[0]) == len(lsi[1]):
            print("=")            
        else:
            print("<")
