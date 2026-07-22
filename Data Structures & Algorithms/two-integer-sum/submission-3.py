class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for r in range(len(nums)):
            n = target - nums[r]
            if n in hash_map:
                return [ hash_map[n] ,r ] 
            hash_map[nums[r]] = r 