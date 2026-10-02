class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # init two pointers on either side of numbers list
        left_pointer = 0
        right_pointer = len(numbers) - 1

        # iterate until both pointers meet
        while left_pointer < right_pointer:
            # current sum to compare against target
            currentSum = numbers[left_pointer] + numbers[right_pointer]

            if currentSum > target:
                # overshot sum so move right pointer back
                right_pointer -= 1
            elif currentSum < target:
                # undershot sum so move left pointer forward
                left_pointer += 1
            else:
                # one-indexed array so add 1 to each index
                return [left_pointer + 1, right_pointer + 1]
        
        return []