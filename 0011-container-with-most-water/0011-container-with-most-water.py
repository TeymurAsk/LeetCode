class Solution:
    def maxArea(self, height: List[int]) -> int:
        mx = 0
        l = 0
        r = len(height) - 1
        while l<r:
            h = min(height[l], height[r])
            if (r-l)*h > mx:
                mx = (r-l)*h
            if height[r] < height[l]:
                r-=1
            else:
                l+=1
        return mx