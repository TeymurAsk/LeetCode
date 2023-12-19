class Solution:
    def mySqrt(self, x: int) -> int:
        for i in range(x+1):
            if i*i > x:
                return i-1
            elif i*i == x:
                return i
        return 0