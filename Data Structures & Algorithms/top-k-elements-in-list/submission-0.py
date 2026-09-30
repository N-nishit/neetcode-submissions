class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        di = {}
        for i in range(len(nums)):
            if nums[i] not in di:
                di[nums[i]] = 1
            else:
                di[nums[i]] += 1
        sorted_data = sorted(di, key=di.get,reverse=True)
        return sorted_data[:k]