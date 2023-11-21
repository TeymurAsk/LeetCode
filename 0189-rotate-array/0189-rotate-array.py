class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        result = []
        for i in range(len(nums)):
            result.append(0)
        pos = k % len(nums)
        for i in range(len(nums)):
            result[(i+pos)%len(nums)] = nums[i]
        nums.clear()
        for i in result:
            nums.append(i)