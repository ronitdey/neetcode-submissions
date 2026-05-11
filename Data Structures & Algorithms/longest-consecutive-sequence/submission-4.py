class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 1
        current = 1
        i = 0

        if len(nums) == 0:
            return 0

        sortedNums = sorted(list(set(nums)))
        
        while i < len(sortedNums)-1:
            if sortedNums[i+1] - sortedNums[i] == 1:
                current += 1
                if current > longest:
                    longest = current
            else:
                if current > longest:
                    longest = current
                    current = 1
                current = 1
            i+= 1
        return longest


        