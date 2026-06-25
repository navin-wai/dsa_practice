class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        output = [0] * len(temp)
        stack = [] #pair [temp , index]

        for i , n in enumerate(temp):
            while stack and n > stack[-1][0]:
                stack_temp , stack_ind = stack.pop()
                output[stack_ind] = (i - stack_ind)
            stack.append([n , i])
        return output
