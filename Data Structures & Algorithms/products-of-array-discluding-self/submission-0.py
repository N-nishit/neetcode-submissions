class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        a = 1
        k = 0
        for i in range(len(nums)):
            if nums[i]!=0:
                a = a*nums[i]
            else:
                k=k+1
        answer = [a]*len(nums)
        for i in range(len(nums)):
            if nums[i]==0 and k==1:
                answer[i]=a
            elif k==len(nums):
                answer[i]=0
            elif 0<k<len(nums):
                answer[i]=0
            else:
                answer[i]=int(answer[i]/nums[i])      
        return answer       
        
