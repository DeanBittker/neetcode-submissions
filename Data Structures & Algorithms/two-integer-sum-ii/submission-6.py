class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        L, R = 0, len(numbers)-1
        while L < R:
            left = numbers[L]
            right = numbers[R]
            if (left + right) > target:
                R -= 1
            elif (left + right) < target:
                L += 1
            else:
                return [L+1, R+1]