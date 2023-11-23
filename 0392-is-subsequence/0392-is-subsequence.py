class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        index = -1
        score = 0
        for i in range(len(s)):
            for j in range(index+1,len(t)):
                if s[i] == t[j]:
                    score+=1
                    index = j
                    break
        if score == len(s):
            return True
        return False