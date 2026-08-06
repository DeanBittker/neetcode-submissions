class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        length = len(nums)
        lower_idx = 0
        higher_idx = length-1
        while(lower_idx<=higher_idx):
            middle_idx = lower_idx + (higher_idx-lower_idx)//2
            if nums[middle_idx] == target:
                return middle_idx
            elif nums[middle_idx] > target:
                higher_idx = middle_idx - 1
            else:
                lower_idx = middle_idx + 1
        return lower_idx


        