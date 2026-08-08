class Solution:
    def trap(self, height: List[int]) -> int:
        maxL, maxR, L, R = 0, 0, 0, len(height)-1
        size = 0
        while L < R:
            if height[L] <= height[R]:
                if (maxL-height[L]) > 0:
                    size += (maxL - height[L])
                else:
                    maxL = height[L]
                L += 1
            else:
                if (maxR-height[R]) > 0:
                    size += (maxR - height[R])
                else:
                    maxR = height[R]
                R -= 1
        return size

