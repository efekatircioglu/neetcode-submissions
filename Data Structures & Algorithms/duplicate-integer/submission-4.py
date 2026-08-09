class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # hasSeen set
        # if num is not in hasSeen: add it to hasSeen
        # if num is in hasSeen: quit looping, return true

        hasSeen = set()
        for num in nums:
            if num in hasSeen:
                return True
            else:
                hasSeen.add(num)


        return False


        