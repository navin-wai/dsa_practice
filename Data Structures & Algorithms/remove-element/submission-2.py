class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        #so we start with two pointers , ptr1 will be at the starting
        #ptr2 will be at the end
        #so we check the first element with ptr1, if equal to two
        #then we check if the value at ptr2 is equal to 2 , if yes we decrement it until we get the value which is not two
        # if no , we swap the two elements and increment ptr1 also k+= 1 
        #if ptr1 not equal to 2 we increment k and ptr1 both

        ptr1 = 0
        ptr2 = len(nums)-1
        k = 0
        if val not in nums:
            return len(nums)
        while ptr1 < ptr2:
            if nums[ptr1] == val:
                while nums[ptr2] == val:
                    ptr2 -= 1
                    if ptr1 == ptr2:
                        break
                temp = nums[ptr1]
                nums[ptr1] = nums[ptr2]
                nums[ptr2] = temp
            else:
                k += 1
                ptr1 += 1
        if k :
            return k
        else : return 0