class Solution:
    def isPalindrome(self, s: str) -> bool:
        L = 0
        a = []
        for char in s:
            if char.isalnum():
                a.append(char.lower())
        R = len(a)-1
        while L < R:
            if a[L] != a[R]:
                return False
            L += 1
            R -= 1
        return True