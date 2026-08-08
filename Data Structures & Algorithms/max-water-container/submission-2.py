class Solution:
    def maxArea(self, heights: List[int]) -> int:
        L=0
        R=len(heights)-1
        max_area = -1
        while L<R:
            if heights[L] <= heights[R]:
                area = heights[L] * (R-L)
                if area > max_area:
                    max_area = area
                L += 1
            elif heights[L] > heights[R]:
                area = heights[R] * (R-L)
                if area > max_area:
                    max_area = area
                R -= 1
        return max_area