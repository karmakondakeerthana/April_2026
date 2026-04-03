class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        dic={}
        for i in s:
            dic[i]=dic.get(i,0)+1
        for ch in t:
            if ch not in dic:
                return False
            dic[ch]-=1
            if dic[ch]<0:
                return False
        return True
                
