class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq = [0] * (max(nums)+1)
        # print(freq)
        for i in nums:
            freq[i] += 1
        m = max(freq)
        res = 0
        for i in freq:
            if i == m:
                res = res + i
        return res