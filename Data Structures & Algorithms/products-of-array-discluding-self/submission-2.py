class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        products_array = [1] * len(nums)

        prefix = 1
        postfix = 1

        for idx in range(len(nums)):
            products_array[idx] = prefix
            prefix *= nums[idx]
        for idx in range(len(nums) - 1, -1, -1):
            products_array[idx] *= postfix
            postfix *= nums[idx]
        
        return products_array