class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # combine in-place slices before and after rotation pivot point
        nums[:] = nums[-k % len(nums):] + nums[:-k % len(nums)]
        