public class Solution {
    public string MergeAlternately(string word1, string word2) {
        StringBuilder rs = new StringBuilder();
        int index = 0;
        int len = 0;

        if (word1.Length > word2.Length)
        {
            len = word2.Length;
        }
        else
        {
            len = word1.Length;
        }

        for (int i = 0; i < len; i++)
        {
            rs.Append(word1[i]);
            rs.Append(word2[i]);
            index = i;
        }

        // Fix the loop condition and append the remaining characters
        for (int i = index + 1; i < word1.Length; i++)
        {
            rs.Append(word1[i]);
        }

        for (int i = index + 1; i < word2.Length; i++)
        {
            rs.Append(word2[i]);
        }

        return rs.ToString();
    }
}