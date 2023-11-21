class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index1 = 0
        index2 = 0
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    index1 = i
                    index2 = j
                    break
        return [index1, index2]