class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = []
        score = 1
        if nums.count(0)>=2:
            return [0]*len(nums)
        for i in range(len(nums)):
            if nums[i] != 0:
                score *= nums[i]
        if nums.count(0) == 1:
            for i in range(len(nums)):
                if nums[i] != 0:
                    answer.append(0)
                else:
                    answer.append(score)
        else:
            for i in range(len(nums)):
                answer.append(score//nums[i])
        return answer