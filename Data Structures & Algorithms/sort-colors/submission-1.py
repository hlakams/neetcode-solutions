class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_idx = 0
        one_idx = 0

        for two_idx in range(len(nums)):
            tmp_val = nums[two_idx]
            nums[two_idx] = 2

            if tmp_val < 2:
                nums[one_idx] = 1
                one_idx += 1
            if tmp_val < 1:
                nums[zero_idx] = 0
                zero_idx += 1
        