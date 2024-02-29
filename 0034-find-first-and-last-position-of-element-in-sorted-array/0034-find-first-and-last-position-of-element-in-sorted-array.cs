public class Solution {
    public int[] SearchRange(int[] nums, int target) {
        int start = -1;
        int end = -1;

        for (int i = 0; i < nums.Length; i++) {
            if (nums[i] == target) {
                start = i;
                break;
            }
        }

        for (int i = nums.Length - 1; i >= 0; i--) {
            if (nums[i] == target) {
                end = i;
                break;
            }
        }

        return new int[] { start, end };
    }
}
