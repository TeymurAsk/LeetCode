class Solution:
    def reverseWords(self, s: str) -> str:
        lst =s.split()
        s1 = ""
        for i in range(len(lst)-1):
            s1 += lst[-i-1]
            s1+= " "
        s1+= lst[0]
        return s1