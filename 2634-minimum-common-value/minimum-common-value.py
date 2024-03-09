class Solution:
    def getCommon(self, nums1, nums2):
        a = defaultdict(int)
        for i in nums1:
            a[i] += 1
        for i in nums2:
            if a[i] > 0:
                return i
        return -1