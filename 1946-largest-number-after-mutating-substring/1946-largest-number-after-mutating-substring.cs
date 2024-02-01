public class Solution {
    public string MaximumNumber(string num, int[] change) {
        int i = 0;
        StringBuilder result = new StringBuilder(num);

        while (i < num.Length && num[i] - '0' >= change[num[i] - '0'])
            i++;

        while (i < num.Length && num[i] - '0' <= change[num[i] - '0']) {
            result[i] = (char)('0' + change[num[i] - '0']);
            i++;
        }

        return result.ToString();
    }
}