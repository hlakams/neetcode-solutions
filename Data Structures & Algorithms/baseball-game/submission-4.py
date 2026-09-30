class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for val in operations:

            if val == "+":
                val_2 = stack.pop()
                val_1 = stack.pop()

                ans = val_1 + val_2

                stack.append(val_1)
                stack.append(val_2)
                stack.append(ans)
            
            elif val == "D":
                stack.append(stack[-1] * 2)
            
            elif val == "C":
                stack.pop()
            
            else:
                stack.append(int(val))
            print(stack)
        
        return sum(stack)
