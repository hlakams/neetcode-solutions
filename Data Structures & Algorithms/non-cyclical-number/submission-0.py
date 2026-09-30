class Solution:
    def isHappy(self, n: int) -> bool:
        def squareSumOfDigits(num: int) -> int:
            ans = 0
            while num > 0:
                ans += (num % 10) ** 2
                num //= 10
            return ans
        
        sum_set = set()
        current_sum = squareSumOfDigits(n)

        while True:
            if current_sum == 1:
                return True
            if current_sum not in sum_set:
                sum_set.add(current_sum)
            else:
                return False

            current_sum = squareSumOfDigits(current_sum)
