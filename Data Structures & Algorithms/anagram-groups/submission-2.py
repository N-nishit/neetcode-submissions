class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        parent_dic = {}
        inner = [0]*26
        for i in strs:
            for j in i:
                inner[ord(j)-97]+=1
            tup = tuple(inner)
            parent_dic.setdefault(tup, []).append(i)
            inner = [0]*26
        return list(parent_dic.values())
       
        