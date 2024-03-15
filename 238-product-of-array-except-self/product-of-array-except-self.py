class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)
        ze = 0
        p = 1
        for i in nums:
            if i == 0:
                ze += 1
        if ze <= 1:
            for i in nums:
                if i != 0:
                    p *= i
            if ze == 1:
                i = nums.index(0)
                ans[i] = p
            else:
                for i in range(0, len(nums)):
                    ans[i] = p//nums[i]
        return ans