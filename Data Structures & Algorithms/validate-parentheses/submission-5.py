class Solution:
    def isValid(self, s: str) -> bool:
        x=""
        for i in range(len(s)):
            if s[i]=="(":
                x=")"+x
            elif s[i]=="[":
                x="]"+x
            elif s[i]=="{":
                x="}"+x
            elif x!="" and ((s[i]==")" and x[0]==")") or (s[i]=="]" and x[0]=="]") or (s[i]=="}" and x[0]=="}")):
                x=x[1:]
            else:
                return False
        if x!="":
            return False
        else:
            return True
                
      
            