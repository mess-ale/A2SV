class Solution:
    def interpret(self, command: str) -> str:
        
        lis = list(command)
        print(lis)
        goal_parser = []
        for i in range(0, len(lis)):
            if lis[i] == 'G':
                goal_parser.append("G")
            elif i == len(lis)-1:
                break
            elif lis[i] == "(" and lis[i+1] == ")":
                goal_parser.append("o")
            elif lis[i] == "(" and lis[i+1] == "a":
                goal_parser.append("al")
            else:
                continue
                
        return "".join(goal_parser)
