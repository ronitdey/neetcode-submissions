class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        n = len(s)
        forward = [] * n
        reverse = [] * n

        for i in range(n):
            if s[i].isalnum():
                forward.append(s[i])
        for i in range(len(s)-1,-1,-1):
            if s[i].isalnum():
                reverse.append(s[i])
        return reverse == forward