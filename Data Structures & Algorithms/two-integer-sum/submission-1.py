class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        data = {}
        twos = []
        for i,x in enumerate(nums):
            data[x] = i
        for i,x in enumerate(nums):
            complement = target - x
            if (complement in data and i != data[complement]):
                twos.append(i)
                twos.append(data[complement])
                return twos