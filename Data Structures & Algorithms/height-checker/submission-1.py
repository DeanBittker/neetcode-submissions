class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        # heights = current order students are in
        # heights[i] is height of i-th student in line
        c=0
        s = sorted(heights)
        for i in range(len(heights)):
            if heights[i] != s[i]:
                c+=1
        return c
