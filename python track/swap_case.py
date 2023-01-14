def swap_case(s):
    
    ss = [i for i in s]
    lis = []
    for s in ss:
        if s.isalpha():
            if s.isupper():
                m = s.lower()
                lis.append(m)
            else:
                m = s.upper()
                lis.append(m)
        else:
            lis.append(s)
            
    return "".join(lis)

if __name__ == '__main__':
