class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sDict = {}
        tDict = {}
        for x in s:
            if x in sDict:
                sDict[x] += 1
            else:
                sDict[x] = 1
        for x in t:
            if x in tDict:
                tDict[x] += 1
            else:
                tDict[x] = 1
        return sDict == tDict