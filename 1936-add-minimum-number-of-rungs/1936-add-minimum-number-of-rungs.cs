public class Solution {
    public int AddRungs(int[] rungs, int dist)
    {
        int result = 0;
        int me = 0;
        for (int i = 0; i < rungs.Length; i++)
        {
            if (me + dist >= rungs[i])
            {
                me = rungs[i];
            }
            else
            {
                while (me + dist < rungs[i])
                {
                    result++;
                    me += dist;
                }
            }
            if (me + dist >= rungs[i])
            {
                me = rungs[i];
            }
        }
        return result;
    }
}