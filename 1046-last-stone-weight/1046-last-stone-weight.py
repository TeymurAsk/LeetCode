class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxheap = []
        for i in stones:
            maxheap.append(-i)
        heapq.heapify(maxheap)
        while len(maxheap)>1:
            maxvalue = heapq.heappop(maxheap)
            minvalue = heapq.heappop(maxheap)
            if maxvalue*(-1) > minvalue*(-1):
                heapq.heappush(maxheap, (maxvalue*(-1)-minvalue*(-1))*(-1))
            elif maxvalue*(-1) < minvalue*(-1):
                heapq.heappush(maxheap, (minvalue*(-1) - maxvalue*(-1))*(-1))
            else:
                continue
        if not maxheap:
            return 0
        return maxheap[0]*-1