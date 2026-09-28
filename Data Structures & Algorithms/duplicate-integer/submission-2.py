class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dict = {}

        for val in nums:
            try:
                dict[val]
                return True
            except:
                dict.setdefault(val, 1)
        
        return False