class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k==0:
            return False
        set_=set()
        for r in range(len(nums)):
            if nums[r] in set_:return True
            set_.add(nums[r])
            if len(set_)==k+1:set_.remove(nums[r-k])
        return False