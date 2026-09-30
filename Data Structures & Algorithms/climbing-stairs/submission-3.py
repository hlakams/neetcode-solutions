class Solution:
    def climbStairs(self, n: int) -> int:
        # use fibonacci; backtrack on 1D array
        fib_array = [1,1,2]

        if n <= 2:
            return fib_array[n]
        
        for idx in range(3, n + 1):
            n_minus_1 = fib_array[2]
            n_minus_2 = fib_array[1]
            fib_array[2] = n_minus_1 + n_minus_2
            fib_array[1] = n_minus_1
            fib_array[0] = n_minus_2
            print(fib_array)

        return fib_array[-1]
        