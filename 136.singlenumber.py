class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        counter = {}
        for i in nums:
            if i in counter:
                counter[i] +=1
            else:
                counter[i] = 1
        for key,values in counter.items():
            if values == 1:
                return key
