class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        for r in range(len(nums)):
            for p in range(len(nums)):
                if r == p:
                    continue
                if nums[r] == nums[p] and (abs(r - p) <= k):
                    return True
        return False 