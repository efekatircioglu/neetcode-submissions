class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # create hashmap{number;index}
        # complement, currentnum, target
        #complement changes every iteration
        # for each number, target-currentnum=complement
        # if complement exist in hashmap, return [numIndex,complementIndex]

        seen = {}
        for index,num in enumerate(nums):
            # seen[num]=index
            complement=target-num
            # print(seen)
            if complement in seen:
                return[seen[complement], index]
            else:
                seen[num]=index
