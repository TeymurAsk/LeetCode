class Solution:
    def trailingZeroes(self, n: int) -> int:
        rst = 0
        while n/5 >=1:
            rst+= n//5
            n = n/5
        return int(rst)