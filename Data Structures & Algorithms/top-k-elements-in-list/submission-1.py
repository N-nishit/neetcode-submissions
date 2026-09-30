class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        di = {}
        bucket = [[] for i in range(len(nums) + 1)]
        out = []
        for i in range(len(nums)):
            if nums[i] not in di:
                di[nums[i]]=1
            else:
                di[nums[i]] += 1

        for i in di:
            bucket[di[i]].append(i)
            
        for i in range(len(bucket)-1,0,-1):
            for j in bucket[i]:
                out.append(j)
                if len(out)==k:
                    return out