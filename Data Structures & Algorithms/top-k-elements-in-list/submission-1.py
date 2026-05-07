class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        data = {}
        topK = []

        for x in nums:
            if x in data:
                data[x] += 1
            else:
                data[x] = 1
        sortedData = sorted(data.items(), key=lambda x: x[1], reverse = True)[0:k]
        
        for i in sortedData:
            topK.append(i[0])
        return topK