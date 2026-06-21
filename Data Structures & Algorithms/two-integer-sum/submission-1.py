class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for n in range(len(nums)):
            sub = target - nums[n]
            if sub in hash_map:
                return[hash_map[sub] , n]
            hash_map[nums[n]] = n