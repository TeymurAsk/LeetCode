public class Solution {
    public int SecondsToRemoveOccurrences(string s) {
        int result = 0;
        while (s.Contains("01"))
        {
            s = s.Replace("01", "10");
            result++;
        }
        return result;
    }
}