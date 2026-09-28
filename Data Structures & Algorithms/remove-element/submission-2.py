class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        tracker_idx = 0

        for idx in range(len(nums)):
            if nums[idx] != val:
                nums[tracker_idx] = nums[idx]
                tracker_idx += 1
        
        return tracker_idx