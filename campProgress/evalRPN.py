class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return int(tokens[0])

        stack = []
        ls = ["+", "/", '*', "-"]
        count = 0
        for i in tokens:
            if i in ls:
                firstnum = int(stack.pop())
                secondnum = int(stack.pop())
                if i == "+":
                    count = firstnum + secondnum
                    stack.append(count)
                elif i == "-":
                    count = secondnum - firstnum
                    stack.append(count)
                elif i == "*":
                    count = firstnum * secondnum
                    stack.append(count)
                elif i == "/":
                    count = int(secondnum / firstnum)
                    stack.append(count)

            else:
                stack.append(i)

        return count
