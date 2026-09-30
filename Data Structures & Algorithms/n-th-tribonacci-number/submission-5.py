class Solution:
    def tribonacci(self, n: int) -> int:
        vals = [0,1,1]

        if n <= 2:
            return vals[n]

        for _ in range(0, n - 3 + 1):
            old_0 = vals[0]
            old_1 = vals[1]
            old_2 = vals[2]

            vals[2] = vals[0] + vals[1] + vals[2]
            
            vals[0] = old_1
            vals[1] = old_2

        return vals[-1]