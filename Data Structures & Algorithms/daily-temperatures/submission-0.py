class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        output = []
        for r in range(len(temp)):
            count = 0
            for n in range(r + 1 , len(temp)):
                if temp[n] > temp[r]:
                    count = n - r
                    break
            output.append(count)
        return output