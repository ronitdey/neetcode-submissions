class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        data = {}
    
        for x in strs:
            count = [0] * 26
            for c in x:
                count[ord(c) - ord("a")] += 1
            key = tuple(count)

            data.setdefault(key, []).append(x)
        
        return list(data.values())
        
    