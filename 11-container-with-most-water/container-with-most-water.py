class Solution:
    def maxArea(self, height: List[int]) -> int:
        startIdx=0
        endIdx=len(height)-1
        area=0
        while endIdx>startIdx:
            area=max(area,min(height[endIdx],height[startIdx]) * (endIdx-startIdx))
            if height[endIdx] > height[startIdx]:
                startIdx+=1
            else:
                endIdx-=1
        return area
