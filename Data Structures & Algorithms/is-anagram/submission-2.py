class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        f={}

        for i in s:
            if i in f:
                f[i] +=1
            else:
                f[i]=1

        for i in t:
            if i not in f:
                return False
            elif f[i]== 1:
                del f[i]
            else:
                f[i]-=1
        return not f