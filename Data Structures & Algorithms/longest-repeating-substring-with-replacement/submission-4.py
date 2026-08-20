from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # sliding window, we can do k replacements, after k replacements 
        # from left to right, every char will be the same (left-to-right k+1 unique characters)
        left=0
        max_so_far=0
        # seen_chars_window = set()
        seen_chars_window = defaultdict(int)

        #  0123
        # "XYYK"


        for right in range(len(s)):
            seen_chars_window[s[right]]= 1 + seen_chars_window.get(s[right],0)
            
            # while windowlength - num of most occurance char > num of possible replacements
            while (right-left + 1) - max(seen_chars_window.values()) > k:
                # shrink the window by removing occurance of chars starting from left letters
                seen_chars_window[s[left]] -=1
                left +=1
            max_so_far = max(max_so_far, right - left + 1)

        
        return max_so_far
