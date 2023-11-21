class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        maxim = 0 
        score = 1
        for i in range(1,len(nums)):
            if nums[i] != nums[i-1]:
                if score > maxim:
                    maxim = score
                    index = i-1
                score = 1
            else:
                score+=1
        if score > maxim:
            return nums[-1]
        return nums[index]