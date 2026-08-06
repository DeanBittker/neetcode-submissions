class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        # key is sorted letters, value is a list of indexes
        for s in strs:
            sorted_str = ''.join(sorted(s))
            if sorted_str not in seen:
                seen[sorted_str] = [s]
            else:
                seen[sorted_str].append(s)
        l = []
        for item in seen.values():
            l.append(item)
        return l
        