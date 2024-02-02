public class Solution {
    
    public int LongestSubstring(string s, int k)
    {
        List<string> list = new List<string>();
        Dictionary<char,int> dict = new Dictionary<char,int>();
        for(int i=0;i<s.Length;i++)
        {
            int val=1;
            if(dict.ContainsKey(s[i]))
            {
                val+=dict[s[i]];
                dict.Remove(s[i]);
            }
            dict.Add(s[i],val);
        }
        StringBuilder sb = new StringBuilder();
        for(int i=0;i<s.Length;i++)
        {
            if(dict.ContainsKey(s[i]) && dict[s[i]]<k)
            {
                sb.Append(s[i]);
                dict.Remove(s[i]);
            }
        }
        string splitChars = sb.ToString();
        list.AddRange(s.Split((splitChars.ToCharArray()),StringSplitOptions.RemoveEmptyEntries));
        if(list.Count==0)
        {
            return 0;
        }
        if(list.Count==1)
        {return list[0].Length;}
        int max=0;
        for(int j=0;j<list.Count;j++)
        {
            max=Math.Max(max,LongestSubstring(list[j],k));
        }
        return max;
    }
}