class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        self = 0
        for x in nums:
            i = 0;
            product = 1;
            while i < len(nums):
                if self != i:
                    product = product * nums[i]
                    i += 1
                else:
                    i += 1
            result.append(product)
            self += 1
        return result