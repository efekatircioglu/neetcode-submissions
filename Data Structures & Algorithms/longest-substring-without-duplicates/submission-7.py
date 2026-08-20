class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # sliding window
        left=0
        maxwindow=0
        seenwindow=set()
        
        # 0123456
        # zxyzxyz
        for right in range(len(s)):
            while s[right] in seenwindow:
                seenwindow.remove(s[left])
                left +=1
            seenwindow.add(s[right])
            maxwindow=max(maxwindow,right-left+1)
        return maxwindow


        