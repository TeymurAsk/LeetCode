class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if not nums:
            return 0

        left, right = 0, 0
        current_sum = 0
        min_length = float('inf')

        while right < len(nums):
            current_sum += nums[right]
            right += 1

            while current_sum >= target:
                min_length = min(min_length, right - left)
                current_sum -= nums[left]
                left += 1

        return 0 if min_length == float('inf') else min_length
