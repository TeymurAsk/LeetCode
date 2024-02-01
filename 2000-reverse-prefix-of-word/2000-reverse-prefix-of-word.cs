public class Solution {
    public string ReversePrefix(string word, char ch) {
        if (word.Contains(ch))
        {
            string result = "";
            for(int i = word.IndexOf(ch); i >=0; i--)
            {
                result += word[i];
            }
            for(int i= word.IndexOf(ch)+1; i<word.Length; i++)
            {
                result += word[i];
            }
            return result;
        }
        return word;
    }
}