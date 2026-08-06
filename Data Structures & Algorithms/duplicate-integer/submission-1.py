class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d = {}
        for item in nums:
            d[item] = 0
        if len(d.keys()) != len(nums):
            return True
        return False