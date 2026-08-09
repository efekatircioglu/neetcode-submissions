class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # case 1) length not same -> False
        # case 2) 
        if len(s) != len(t):
            return False

        s_dict = {}
        t_dict = {}
        for i in s:
            s_dict[i] = s_dict.get(i,0) + 1
        for i in t:
            t_dict[i] = t_dict.get(i,0) + 1
        
        for i in s_dict:
            if s_dict[i] != t_dict.get(i,0):
                return False
        return True

        



        