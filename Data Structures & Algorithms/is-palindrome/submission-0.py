class Solution:
    def isPalindrome(self, s: str) -> bool:
        x=""
        for i in s:
            if i.isalnum():
                if i.isupper():
                    x=x+i.lower()
                else:
                    x=x+i
            
        for i in range(int(len(x)/2)):
            if x[i]!=x[len(x)-1-i]:
                return False
        return True
