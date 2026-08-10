class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # in place for a given number, the number turns into the product of array exept that num
        res = [1] * len(nums)
        prefix=1

        # start: [1,1,1,1]
        # step1: [1,1,1,1]
        # step2: [2,1,2,2]
        # step3: [8,4,2,8]
        # step4: [48,24,12,8]

        for index, number in enumerate(nums):
            # 0,1
            # 1,2
            # 2,4
            # 3,6

            # index 0 -> index 1 * index 2 * index 3
            # index 1 -> index 0 ....
            # at each step, multiply everything in list with current number besides the same index with res array
            # everything up to [:index] and [index+1:]
            res[index]=prefix
            prefix *= nums[index]
        postfix=1

        for i in range(len(nums)-1,-1,-1):
            res[i] *= postfix
            postfix *= nums[i]
        return res
            


