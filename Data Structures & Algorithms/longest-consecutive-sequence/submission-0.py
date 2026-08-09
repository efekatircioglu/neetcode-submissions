class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # input = unordered list of integers
        # output = number of unique longest consecutive sequence

        # start of consecutive = given a num, num-1 does not exist
        # [num, num+1, num+2...]
        numSet= set(nums)
        maxLength = 0
        for i in nums:
            # check if i is the start of a sequence
            if i-1 not in numSet:
                length = 0
                while i+length in numSet:
                    length +=1
                maxLength = max(maxLength, length)
        return maxLength

