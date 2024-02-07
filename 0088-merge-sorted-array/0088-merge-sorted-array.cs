public class Solution {
    public void Merge(int[] nums1, int m, int[] nums2, int n) {
        for (int j=0; j<n; j++){
            nums1[m+j] = nums2[j];
        }
        Array.Sort(nums1);
    }
}