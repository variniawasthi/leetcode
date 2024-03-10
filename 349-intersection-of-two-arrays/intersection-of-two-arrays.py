class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        a1 = set(nums1)
        a2 = set(nums2)
        m = max(nums1)
        if m < max(nums2):
            m = max(nums2)
        freq = [0] * (m+1)
        for i in a1:
            freq[i] += 1
        for i in a2:
            freq[i] += 1
        res = []
        for i in range(0, len(freq)):
            if freq[i] > 1:
                res.append(i)
        return res