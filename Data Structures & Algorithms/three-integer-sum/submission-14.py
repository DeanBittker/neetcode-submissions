class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        answers = []
        for i in range(len(nums)):
            if i > 0 and sorted_nums[i] == sorted_nums[i-1]: continue
            L = i + 1
            R = len(sorted_nums)-1
            num = sorted_nums[i]
            while L < R:
                left = sorted_nums[L]
                right = sorted_nums[R]
                if left + right + num > 0:
                    R -= 1
                elif left + right + num < 0:
                    L += 1
                else:
                    answers.append([left, right, num])
                    L += 1
                    R -= 1
                    while L < R and sorted_nums[L] == sorted_nums[L-1]: L+=1        
        return answers