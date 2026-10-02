class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        p = [1]*len(nums)
        s = [1]*len(nums)
        answer = [1]*len(nums)
        p[0]=nums[0]
        s[-1]=nums[-1]
        for i in range(1,len(nums)):
            p[i] = p[i-1]*nums[i]
            s[len(nums)-1-i]=s[len(nums)-i]*nums[len(nums)-i-1]
        for i in range(len(nums)):
            if i==0:
                answer[i]=s[i+1]
            elif i==len(nums)-1:
                answer[i]=p[i-1]
            else:
                answer[i]=p[i-1]*s[i+1]
        return answer