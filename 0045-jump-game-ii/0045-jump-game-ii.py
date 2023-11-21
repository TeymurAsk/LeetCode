class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        max_reach = nums[0]  # Maximum reachable position
        steps = 1  # Initial step count
        max_pos = nums[0]  # Maximum position that can be reached with the current steps
        for i in range(1, len(nums)):
            if i > max_pos:  # If the current position exceeds the maximum reachable position, 
                steps += 1
                max_pos = max_reach
            max_reach = max(max_reach, i + nums[i]) 
        return steps