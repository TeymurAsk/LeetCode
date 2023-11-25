class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        lst1 = []
        lst2 = []
        for i in range(len(s)):
            lst1.append(s.index(s[i]))
            lst2.append(t.index(t[i]))
        if lst1 == lst2:
            return True
        return False