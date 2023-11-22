class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""
        work = ""
        min = len(strs[0])
        for i in strs:
            if len(i) <= min:
                work = i
                min = len(i)
        for i in range(len(work)):
            for j in range(len(strs)):
                if strs[j][:len(work)-i] == work[:len(work)-i]:
                    result = work[:len(work)-i]
                else:
                    result = ""
                    break
            if result != "":
                return result
        return result