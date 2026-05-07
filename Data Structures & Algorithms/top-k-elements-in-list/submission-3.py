class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        minHeap = []

        for key,value in count.items():
            heapq.heappush(minHeap,(value,key))
            while len(minHeap) > k:
                heapq.heappop(minHeap)
        
        return [val[1] for val in minHeap]