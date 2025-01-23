class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        def _helper(ind,ans,curr,comb):

            if ind == len(digits):
                ans.append(curr)
                return
            

            s = comb[int(digits[ind])]

            

            for char in s:

                _helper(ind+1,ans,curr+char,comb)

                

        comb = ["","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
        ans = []


        if not digits:
            return ans

        _helper(0,ans,"",comb)

        return ans