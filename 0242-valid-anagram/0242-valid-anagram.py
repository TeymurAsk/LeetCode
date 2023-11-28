class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            if t.count(s[i]) != s.count(s[i]):
                return False
        return True