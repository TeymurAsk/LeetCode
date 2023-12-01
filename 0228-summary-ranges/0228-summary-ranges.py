class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        tmp = []
        res = []
        if nums == []:
            return []
        if len(nums) == 1:
            return [f"{nums[0]}"]
        for i in range(len(nums)-1):
            if nums[i]+1 == nums[i+1]:
                tmp.append(nums[i])
            else:
                tmp.append(nums[i])
                if len(tmp) == 1:
                    res.append(f"{tmp[0]}")
                    tmp = []
                else:
                    res.append(f"{tmp[0]}->{tmp[-1]}")
                    tmp = []
        if nums[-1]-1 == nums[-2]:
            tmp.append(nums[-1])
            res.append(f"{tmp[0]}->{tmp[-1]}")
        else:
            res.append(f"{nums[-1]}")  
        return res