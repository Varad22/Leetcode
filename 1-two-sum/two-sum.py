class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index=[]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j] == target and i not in index:
                    print(i,j)
                    index.append(i)
                if nums[i]+nums[j] == target and j not in index:
                    print(i,j)
                    index.append(j)
        return index
