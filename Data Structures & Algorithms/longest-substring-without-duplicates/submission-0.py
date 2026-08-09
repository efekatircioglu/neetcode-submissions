class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # sliding window vars length
        # outer for right in range(len[arr])
        # inner while for condition_violation
        # update result after quiting while

        # create a set

        resultSet = set()
        left = 0
        res=0

        for right in range(len(s)):
            while s[right] in resultSet:
                resultSet.remove(s[left])
                left +=1
            resultSet.add(s[right])
            res = max(res,right-left+1)
        
        return res

            