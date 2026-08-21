from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # letters of s1 (in any order) should be in s2
        # hashmap of s1 letter-> int
        if len(s1)>len(s2):
            return False
        left=0
        s1_map = defaultdict(int)
        s2_window_map = defaultdict(int)
        # sliding window of length len(s1)
        # if every char in that window is in s1: true, else move window by 1
        for letter in s1:
            s1_map[letter] +=1

        for right in range(len(s2)):
            

            # add to hashmap
            s2_window_map[s2[right]] +=1
            
            # windowlength > len(s1): remove left char
            while (right - left + 1)> len(s1):
                # -1 if value>0
                s2_window_map[s2[left]] -=1 
                if s2_window_map[s2[left]] == 0:
                    del s2_window_map[s2[left]]
                left +=1

            # trigger
            if s1_map == s2_window_map:
                return True
            
                
        return False



# abc.  vs lecabee
# s1= a1 b1 c1

# 1) l1
# 2) l1 e1
# 3) l1 e1 c1
# 4) e1 c1 a1
# 5) c1 a1 b1


# ab.  vs lecabee
# s1= a1 b1

# 1) l1
# 2) l1 e1
# 3) e1 c1 
# 4) c1 a1
# 5) a1 b1
# 6) b1 e1
# 7) e2


            



        