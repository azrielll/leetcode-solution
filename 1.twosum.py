class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i,j in enumerate(nums):
            hasil = target - j
            if hasil in hashmap:
                return hashmap[hasil],i
            hashmap[j] = i
