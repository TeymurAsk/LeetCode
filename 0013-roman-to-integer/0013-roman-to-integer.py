class Solution:
    def romanToInt(self, s: str) -> int:
        score = 0
        dct = {"I":1, "V":5, "X":10,"L":50,"C":100,"D":500,"M":1000}
        for i in range(1,len(s)):
            if dct[s[i]] <= dct[s[i-1]]:
                score+=dct[s[i]]
            elif dct[s[i]] > dct[s[i-1]]:
                score += dct[s[i]] - dct[s[i-1]] - dct[s[i-1]]
        score += dct[s[0]]
        return score