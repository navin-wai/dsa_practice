class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hash_map = {}

        for i in range(len(nums)):
            hash_map[nums[i]] = 1 + hash_map.get(nums[i] , 0)
        
        for key , value in hash_map.items():
            if value > len(nums)/2:
                return key