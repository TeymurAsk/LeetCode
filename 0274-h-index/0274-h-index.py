class Solution:
    def hIndex(self, citations: List[int]) -> int:
        step = 0
        citations.sort()
        if len(citations) == 1 and citations[0] !=0:
            return 1
        for i in range(len(citations)-1, -1,-1):
            if citations[i] > step:
                step+=1
            else:
                return step
        if step > 0:
            return step
        return 0