class Solution:

    def encode(self, strs: List[str]) -> str:
        k=""
        if len(strs)==0:
            print(1)
            return ""
        elif strs==[""]:
            print(2)
            return "`$"
        print(3)
        for i in range(len(strs)):
            if i==len(strs)-1:
                k=k+strs[i]
                break
            k=k+strs[i]+"`"
        print(k)
        return k
    def decode(self, s: str) -> List[str]:
        
        if s=="":
            return []
        elif s=="`$":
            return [""]
        else:
            return s.split("`")