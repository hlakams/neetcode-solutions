class Solution:
    def tribonacci(self, n: int) -> int:
        vals = [0,1,1]
        current_idx = 0

        if n <= 2:
            return vals[n]

        while current_idx <= n - 3:
            old_0 = vals[0]
            old_1 = vals[1]
            old_2 = vals[2]

            vals[2] = vals[0] + vals[1] + vals[2]
            
            vals[0] = old_1
            vals[1] = old_2

            current_idx += 1

        return vals[-1]