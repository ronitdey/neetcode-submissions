class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        result = []

        buckets = [[] for i in range(len(nums)+ 1)]
        for num,count in count.items():
            buckets[count].append(num)
        
        for freq in range(len(buckets)-1,0,-1):
            for num in buckets[freq]:
                result.append(num)
            if len(result) == k:
                return result