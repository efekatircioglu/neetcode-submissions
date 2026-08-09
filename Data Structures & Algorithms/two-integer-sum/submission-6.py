class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {} #value;index
        # for each number, if complement exist in seen: return [compIndex,currindex]
        # if not: seen[nums[index]]=index
        for i in range(len(nums)):
            goal = target - nums[i]
            if goal in seen:
                return[seen[goal],i]
            seen[nums[i]]=i
            
