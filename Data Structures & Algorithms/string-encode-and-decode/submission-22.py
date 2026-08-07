class Solution:

    def encode(self, strs: List[str]) -> str:
        str1 = str(len(strs)) + "#"
        for item in strs:
            str1 += (str(len(item)) + "#" + item)
        return str1

    def decode(self, s: str) -> List[str]:
        l = []
        idx = 0
        while s[idx] != "#":
            idx += 1
        rep = int(s[:idx])
        idx += 1
        for i in range(rep):
            num=[]
            while True:
                if s[idx] != "#":
                    num.append((s[idx]))
                    idx+=1
                else:
                    idx+=1
                    break
            n = "".join(num)
            n = int(n)
            l.append(s[idx:(idx+n)])
            idx = idx+n
        return l





            

            


