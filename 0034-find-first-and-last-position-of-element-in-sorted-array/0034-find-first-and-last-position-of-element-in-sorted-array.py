class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = -1
        end = -1
        for i in range(len(nums)):
            if nums[i] == target:
                start = i
                break
        for i in range(len(nums)-1, -1, -1):
            if nums[i] == target:
                end = i
                break
        return [start, end]