class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        
        if n == 0:
            return 0

        nums.sort()

        cnt = 1
        maxi = 0

        for i in range(1, n):
            if nums[i] != nums[i - 1]:
                if nums[i] == nums[i - 1] + 1:
                    cnt += 1
                else:
                    maxi = max(maxi, cnt)
                    cnt = 1

        return max(maxi, cnt)
