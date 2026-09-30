class Solution:
    def simplifyPath(self, path: str) -> str:
        # stack of entity strings
        stack = []

        for char in path:
            print(stack)
            # init stack
            if not stack:
                stack.append(char)
                continue
            
            if stack[-1] == "/":
                if char == "/":
                    continue
                else:
                    stack.append(char)
                    continue
            elif stack[-1] == ".":
                if char == ".":
                    stack.append(stack.pop() + char)
                    continue
                elif char == "/":
                    stack.pop()
                    stack.pop()
                    stack.append(char)
                    continue
                else:
                    stack.append(stack.pop() + char)
                    continue
            elif stack[-1] == "..":
                if char == ".":
                    stack.append(stack.pop() + char)
                    continue
                elif char == "/":
                    stack.pop()
                    stack.pop()
                    if stack:
                        stack.pop()
                        stack.pop()
                    stack.append(char)
                    
                    continue
                else:
                    stack.append(stack.pop() + char)
                    continue
            else:
                if char == '/':
                    stack.append(char)
                    continue
                else:
                    stack.append(stack.pop() + char)
                    continue
        if stack[-1] == "..":
            stack.pop()
            stack.pop()
            if len(stack) > 1:
                stack.pop()
        if stack[-1] == ".":
            stack.pop()
        if len(stack) > 1 and stack[-1] == "/":
            return "".join(stack[0:-1])
        else:
            return "".join(stack)