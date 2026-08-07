class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_sum=[nums[0]]
        postfix_sum=[1] * len(nums)
        postfix_sum[-1] = nums[-1]
        for i in range(1, len(nums)):
            prefix_sum.append(nums[i]*prefix_sum[-1])
        for i in range(len(nums)-2,-1,-1):
            postfix_sum[i] = nums[i] * postfix_sum[i+1]
        solution = [1]*len(nums)
        solution[0] = postfix_sum[1]
        for i in range(1, len(nums)-1):
            solution[i] = postfix_sum[i+1] * prefix_sum[i-1] 
        solution[-1] = prefix_sum[-2]
        return solution
