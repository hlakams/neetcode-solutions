class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # init dict for count of appearances + list for nums per hit
        count = {}
        frequency = [[] for _ in range(len(nums) + 1)]

        # find appearances of each number
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        # map appearances to numbers
        for num, count in count.items():
            frequency[count].append(num)
        
        ans = []
        for idx in range(len(frequency) - 1, 0, -1):
            for num in frequency[idx]:
                ans.append(num)
                
                if len(ans) == k:
                    return ans