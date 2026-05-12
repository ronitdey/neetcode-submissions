class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        
        for i in range(len(nums)):
            target = -(nums[i])
            left = i + 1
            right = len(nums) - 1

            while left < right:
                if nums[left] + nums[right] == target:
                    if [nums[i],nums[left],nums[right]] in result:
                        left += 1
                        right -= 1
                    else:
                        result.append(list([nums[i],nums[left],nums[right]]))
                        left += 1
                        right -= 1
                elif nums[left] + nums[right] < target:
                    left += 1
                else:
                    right -= 1
    
        return result
        