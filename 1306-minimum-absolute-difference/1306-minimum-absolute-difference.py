class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        ret = []
        arr.sort()
        absMin = float('inf')

        for i in range(len(arr) - 1):
            absMin = min(absMin, abs(arr[i+1] - arr[i]))

        for i in range(1, len(arr)):
            if arr[i] - arr[i-1] == absMin:
                ret.append([arr[i-1], arr[i]])

        return ret