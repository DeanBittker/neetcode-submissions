class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        seen = {}
        counter = 0
        for item in arr:
            if item not in seen:
                seen[item] = 1
            else:
                seen[item] += 1
        for item in arr:
            if seen[item] == 1:
                counter +=1
            if counter == k:
                return item
        return ""

        