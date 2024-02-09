public class Solution {
    public int[] TwoSum(int[] numbers, int target) {
        int i = 0;
        int j = numbers.Count() - 1;
        while (true){
            if (numbers[i] + numbers[j] == target)
                return [i+1, j+1];
            if (numbers[i] + numbers[j] > target)
                j-=1;
            else if (numbers[i] + numbers[j] < target)
                i+=1;
        }
    }
}