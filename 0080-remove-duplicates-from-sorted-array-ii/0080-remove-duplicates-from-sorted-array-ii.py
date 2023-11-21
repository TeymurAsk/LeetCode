class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums1 = [nums[0]]
        tmp = 1
        for i in range(1,len(nums)):
            if nums[i] != nums[i-1]:
                nums1.append(nums[i])
                tmp = 1
            else:
                if tmp < 2:
                  nums1.append(nums[i])
                  tmp+=1  
        nums.clear()
        for i in nums1:
            nums.append(i)
        return len(nums)