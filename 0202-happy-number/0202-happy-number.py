class Solution:
    def isHappy(self, n: int) -> bool:
        n = str(n)
        tmp = 0
        for j in range(100):
            for i in range(len(n)):
                tmp += int(n[i])*int(n[i])
            if tmp == 1:
                return True
            else:
                n=str(tmp)
                tmp = 0
        return False