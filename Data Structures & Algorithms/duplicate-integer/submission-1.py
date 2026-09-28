class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        entry_dict = defaultdict(int)

        for val in nums:
            entry_dict[val] += 1
            if entry_dict[val] > 1:
                return True
        
        return False
        