class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        res , max_count = 0 , 0

        for n in nums:
            count[n] = 1 + count.get(n , 0)
            if count[n] > max_count:
                res = n
            max_count = max(count[n], max_count)
        return res