class Solution:
    def maxArea(self, height: list[int]) -> int:
        l=0
        r=len(height)-1
        area=0
        while l<r:
            if height[l]>height[r]:
                if area<(r-l)*height[r]:
                    area=(r-l)*height[r]
                r=r-1
            else:
                if area<(r-l)*height[l]:
                    area=(r-l)*height[l]
                l=l+1
        return area

            
            