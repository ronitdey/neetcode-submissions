class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        preFix = []
        postFix = []
        result = []

        preProduct = 1
        postProduct = 1

        for i in range (0,len(nums),1):
            preProduct = preProduct * nums[i]
            preFix.append(preProduct)

        for i in range (len(nums)-1,-1,-1):
            postProduct = postProduct * nums[i]
            postFix.append(postProduct)
        postFix.reverse()

        for i in range(len(nums)):
            if i-1 != -1 and i+1 < len(nums):
                result.append(preFix[i-1]*postFix[i+1])
            elif i-1 == -1:
                result.append(postFix[i+1])
            elif i+2 > len(nums):
                result.append(preFix[i-1])
        return result
                
    