class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        cur_level = []
        num = 0
        
        for char in s:
            if char.isdigit():
                num = num * 10 + int(char)
            
            elif char.isalpha():
                cur_level.append(char)
            
            elif char == '[':
                stack.append((num, [*cur_level]))
                cur_level = []
                num = 0
            
            elif char == ']':
                prev_level_num, prev_level = stack.pop()
                cur_level_string = "".join(cur_level)
                cur_level = [*prev_level, prev_level_num * cur_level_string] 
            
        return "".join(cur_level)