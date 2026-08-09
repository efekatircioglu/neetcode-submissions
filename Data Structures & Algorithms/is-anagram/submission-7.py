class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # hasmap for s:  letter to occurence
        # another hasmap for t
        sMap = {}
        tMap= {}

        for letter in s:
            sMap[letter]= 1+ sMap.get(letter,0)
        for letter in t:
            tMap[letter] = 1 + tMap.get(letter,0)        
        return sMap == tMap
