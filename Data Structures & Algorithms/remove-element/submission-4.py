class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        tracker_idx = 0

        for num_val in nums:
            if num_val is not val:
                nums[tracker_idx] = num_val
                tracker_idx += 1
        
        return tracker_idx