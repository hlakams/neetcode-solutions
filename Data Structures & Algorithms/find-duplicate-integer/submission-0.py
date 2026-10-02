class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums_set = set()

        for val in nums:
            if val not in nums_set:
                nums_set.add(val)
            else:
                return val
        
        return 0