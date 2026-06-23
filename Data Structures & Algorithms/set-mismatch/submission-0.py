class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        
        res = [0 , 0]

        count = Counter(nums) #returns the freq of nums ,and if the number not present it will return 0 , instead of a error

        for n in range(1, len(nums)+1):#since the n starts from 1 to n+1
            if count[n] == 2:
                res[0] = n
            if count[n] == 0:
                res[1] = n
        return res