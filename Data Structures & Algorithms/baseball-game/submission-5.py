class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        ans = 0

        for val in operations:

            if val == "+":
                val_2 = stack.pop()
                val_1 = stack.pop()

                sum = val_1 + val_2

                stack.append(val_1)
                stack.append(val_2)
                stack.append(sum)
            
            elif val == "D":
                stack.append(stack[-1] * 2)
            
            elif val == "C":
                stack.pop()
            
            else:
                stack.append(int(val))
            print(stack)
        
        while stack:
            ans += stack.pop()
        
        return ans

