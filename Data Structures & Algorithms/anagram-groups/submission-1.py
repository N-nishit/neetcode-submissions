class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        parent_dic = {}
        inner = [0]*26
        for i in strs:
            for j in i:
                inner[ord(j)-97]+=1
            tup = tuple(inner)
            if tup not in parent_dic:
                parent_dic[tup] = []
                parent_dic[tup].append(i)
            else:
                parent_dic[tup].append(i)
            inner = [0]*26
        return list(parent_dic.values())
       
        