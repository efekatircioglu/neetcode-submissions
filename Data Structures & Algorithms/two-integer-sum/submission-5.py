class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # create seen hashmap value;index
        # for each number, if complement exist in hashmap, return [compIndex,currentIndex]
        # if not exist, add them to hashmap [value,index]

        seen={}
        for index,value in enumerate(nums):
            complement = target - value
            if complement in seen:
                return [seen[complement],index]
            seen[value]=index

        