class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        hash_set = set()
        res = []

        for n in nums:
            hash_set.add(n)
        for n in range(1 , len(nums)+1):
            if n not in nums:
                res.append(n)
        return res