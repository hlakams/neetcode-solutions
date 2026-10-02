class Solution:
    def maxArea(self, heights: List[int]) -> int:
        leftPointer = 0
        rightPointer = len(heights) - 1
        currentMax = 0

        while leftPointer < rightPointer:
            area = min(heights[leftPointer], heights[rightPointer]) * (rightPointer - leftPointer)
            currentMax = max(currentMax, area)

            if heights[leftPointer] <= heights[rightPointer]:
                leftPointer += 1
            else:
                rightPointer -= 1
        
        return currentMax