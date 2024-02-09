using System.Text.RegularExpressions;
public class Solution {
    public string ReverseWords(string s) {
        string[] words = s.Split(' ');
        Array.Reverse(words);
        string result = string.Join(' ', words);
        string cleanedString = Regex.Replace(result.Trim(), @"\s+", " ");
        return cleanedString;
    }
}