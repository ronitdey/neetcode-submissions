class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 1
        left = 0
        right = 0
        seen = set()

        if len(s) == 0:
            return 0

        while right < len(s):
            if s[right] not in seen:
                seen.add(s[right])
                longest = max(longest,len(seen))
                right += 1
            else:
                while s[right] in seen:
                    seen.remove(s[left])
                    left += 1
        return longest

        