class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = n - 2
        # find the index i until nums[i] >= nums[i+1]
        while i >= 0 and nums[i] >= nums[i+1]:
            i -= 1
        if i >= 0:
            # find the smallest element just larger than nums[i] from right
            j = n-1
            while nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        # Reverse subarray to the right of i
        nums[i+1:]  = nums[i+1:][::-1]       