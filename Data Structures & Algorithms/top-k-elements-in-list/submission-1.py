class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)  # form here we have 3 = 2times
        for (n,c) in count.items():  # here c is the count, and n in the number,
            #n is the key in count and c is the value but in the next line we change it
            freq[c].append(n)  # now here making it like 2time -> [3, can add more..]

        res = []
        for i in range(len(freq) - 1, 0, -1):#from the last elemnet to 0, by doing -1
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res