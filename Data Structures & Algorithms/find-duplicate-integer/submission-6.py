class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums_set = {}

        for idx in range(len(nums)):
            if nums[idx] not in nums_set:
                nums_set[nums[idx]] = idx
            else:
                return nums[idx]