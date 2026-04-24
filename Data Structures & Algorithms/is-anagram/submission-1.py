class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False

        freq_char={}
        for i in s:
            freq_char[i] = freq_char.get(i,0)+1
        
        for c in t:
            if c not in freq_char:
                return False
            freq_char[c] -=1
            if freq_char[c]==0:
                del freq_char[c]
            
        return len(freq_char)==0