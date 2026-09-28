class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        nums_freq = Counter(nums)
        ans = []

        for num in nums_freq:
            if nums_freq[num] > len(nums) // 3:
                ans.append(num)
        
        return ans