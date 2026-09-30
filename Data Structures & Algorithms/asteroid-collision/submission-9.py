class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for val in asteroids:
            while stack and val < 0 and stack[-1] > 0:
                sum = val + stack[-1]

                if sum < 0:
                    stack.pop()
                elif sum > 0:
                    val = 0
                else:
                    val = 0
                    stack.pop()
            
            if val:
                stack.append(val)
        
        return stack