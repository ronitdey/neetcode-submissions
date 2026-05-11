class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        result = []
        leftPointer = 0
        RightPointer = len(numbers) - 1

        while leftPointer < RightPointer:
            if numbers[leftPointer] + numbers[RightPointer] == target:
                result.append(leftPointer+1)
                result.append(RightPointer+1)
                return result
            elif numbers[leftPointer] + numbers[RightPointer] > target:   
                RightPointer -= 1
            elif numbers[leftPointer] + numbers[RightPointer] < target:
                leftPointer += 1

        return result
        

