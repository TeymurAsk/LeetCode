class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        maxim = 0
        index = 0
        for i in range(len(arr)):
            if arr.count(arr[i])>maxim:
                maxim =arr.count(arr[i])
                index = i
        return arr[index]