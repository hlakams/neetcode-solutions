class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # map to keep track of indices for numbers we've already seen
        dupe_map = {}

        for idx, val in enumerate(nums):
            # check if number already seen and if indices satisfy inequality
            if val in dupe_map and idx - dupe_map[val] <= k:
                return True
            # else set seen index for current number
            dupe_map[val] = idx

        return False 
        