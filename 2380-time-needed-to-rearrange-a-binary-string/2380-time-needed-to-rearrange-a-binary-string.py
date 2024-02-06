class Solution:
    def secondsToRemoveOccurrences(self, s: str) -> int:
        result = 0
        while s.find("01")!=-1:
            s = s.replace("01","10")
            result+=1
        return result  