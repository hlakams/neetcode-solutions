class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        values_stack = []

        for token in tokens:
            if token == "+":
                val_2 = values_stack.pop()
                val_1 = values_stack.pop()
                values_stack.append(val_1 + val_2)
            elif token == "-":
                val_2 = values_stack.pop()
                val_1 = values_stack.pop()
                values_stack.append(val_1 - val_2)
            elif token == "*":
                val_2 = values_stack.pop()
                val_1 = values_stack.pop()
                values_stack.append(val_1 * val_2)
            elif token == "/":
                val_2 = values_stack.pop()
                val_1 = values_stack.pop()
                values_stack.append(int(val_1 / val_2))
            else:
                values_stack.append(int(token))
        
        return values_stack[0]