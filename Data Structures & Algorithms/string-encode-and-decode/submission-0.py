class Solution:

    def encode(self, strs: List[str]) -> str:
        results=""
        for word in strs:         #format = 5#hello
            results+=str(len(word)) + "#" + word
        
        return results

    def decode(self, s: str) -> List[str]:
        results=[]
        i=0
        while i < len(s):
            j=i
            while s[j]!= "#":
                j+=1
            length= int(s[i:j])
            results.append(s[j+1: length+j+1])
            i=j+length+1
        return results