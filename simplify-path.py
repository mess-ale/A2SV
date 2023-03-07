class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for dir_name in path.split('/'):
            if dir_name == '' or dir_name == '.':
                continue
            elif dir_name == '..':
                if stack:
                    stack.pop()
                else:
                    continue
            else:
                stack.append(dir_name)
                
        return '/' + '/'.join(stack)