class Solution:
    def maxProfit(self, nums: List[int]) -> int:
        
        l = 0
        r = 1
        max_sum = 0

        while r != len(nums):
            if nums[r] > nums[l]:
                max_sum = max(max_sum , nums[r] - nums[l])
            else:
                l = r
            r += 1 

        return max_sum