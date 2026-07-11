class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        res = []
        freqMap = Counter(arr1)

        for a in arr2:
            res.extend([a] * freqMap[a])
            freqMap.pop(a)

        for k in sorted(freqMap.keys()):
            res.extend([k] * freqMap[k])

        return res