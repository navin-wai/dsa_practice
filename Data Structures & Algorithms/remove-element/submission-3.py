class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        # if nums at i is not equal to value, we change that nums k
        # with nums[i] and then increment 
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k