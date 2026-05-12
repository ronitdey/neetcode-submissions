class Solution:
    def maxArea(self, heights: List[int]) -> int:
        current = 0
        left = 0
        right = len(heights) - 1

        while left < right:
            height = min(heights[left],heights[right])
            width = right - left
            area = height * width
            current = max(current,area)

            if heights[left] < heights[right]:
                left+= 1
            elif heights[left] > heights[right]:
                right -= 1
            else:
                left += 1
                right -= 1
        return current
        