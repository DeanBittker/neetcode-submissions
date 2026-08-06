class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = {}
        for num in nums:
            seen[num] = 0
        maximum = 0
        for key in seen.keys():
            if key - 1 not in seen:
                length = 1
                while (key + length) in seen:
                    length +=1
                if length > maximum:
                    maximum = length
        return maximum
            
        