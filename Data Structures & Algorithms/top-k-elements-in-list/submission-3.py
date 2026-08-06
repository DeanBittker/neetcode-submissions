class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        for item in nums:
            if item not in seen:
                seen[item] = 1
            else:
                seen[item] += 1
        l=[]
        for key,value in seen.items():
            l.append((value,key))
        s = sorted(l)
        a=[]
        while k > 0:
            t = s.pop()
            a.append(t[1])
            k -= 1
        return a

                
            
