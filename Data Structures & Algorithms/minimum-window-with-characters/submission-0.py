from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        answer = ""
        resLen=len(s) +1

        t_map = defaultdict(int)
        s_window=defaultdict(int)

        # add letters into t_map
        for letter in t:
            t_map[letter] += 1
        
        have, need = 0, len(t_map)
        l=0
        res=[-1,-1]
        for r in range(len(s)):
            # add letters into s_window
            s_window[s[r]] += 1
            
            # if current letter is in tmap and their required counts are same increase have
            if s[r] in t_map and s_window[s[r]] == t_map[s[r]]:
                have +=1
            
            while have == need:
                # window length < resLen:
                if (r-l+1) < resLen:
                    res=[l,r]
                    resLen=r-l+1

                s_window[s[l]] -=1
                if s[l] in t_map and s_window[s[l]] < t_map[s[l]]:
                    have -=1
                l +=1
        l,r=res
        return s[l:r+1] if resLen < len(s)+1 else ""

    


            


        # from left to right, start adding letters into s_window_map. If letters on left/right is not a requirement, remove them.
        # when all the requirements have done, if current_window_range < shortest: shortest=current_window_range
        # return shortest
        