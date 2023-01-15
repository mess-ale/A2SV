class Solution:
    def freqAlphabets(self, s: str) -> str:
        lis = ['a','b','c','d','e','f','g',"h",'i']
        dic1 = {}
        for i in range(1,10):
            dic1[i] = lis[i-1]
        dic2 = {}
        lis = ['j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        for i in range(10, 10+len(lis)):
            ld = "{}#".format(i)
            dic2[ld] = lis[i-10]
        given_list = [i for i in s]
        stack = []
        for i in range(0, len(s)):
            if given_list[i] != "#":
                stack.append(given_list[i])
            else:
                stack.pop()
                stack.pop()
                stack.append(''.join(given_list[i-2:i+1]))
        alphabet_answer = []
        for i in stack:
            if len(i) == 1:
                alphabet_answer.append(dic1[int(i)])
            else:
                alphabet_answer.append(dic2[i])
        return "".join(alphabet_answer)
            
