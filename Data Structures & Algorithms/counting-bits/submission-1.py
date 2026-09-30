class Solution:
    def countBits(self, n: int) -> List[int]:
        one_bits = []
        for num in range(0, n + 1):
            ans = 0
            while num:
                num &= num - 1
                ans += 1
            one_bits.append(ans)
        
        return one_bits