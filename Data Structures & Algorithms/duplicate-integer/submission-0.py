class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            x=nums.pop()
            if x in nums:
                return True
        return False