class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # map to keep track of indices for numbers we've already seen
        dupe_map = {}

        for idx in range(len(nums)):
            # check if number already seen and if indices satisfy inequality
            if nums[idx] in dupe_map and idx - dupe_map[nums[idx]] <= k:
                return True
            # else set seen index for current number
            dupe_map[nums[idx]] = idx

        return False 
        