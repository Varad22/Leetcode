class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lst=[]
        lengths=[]
        value=0
        if len(s)>0:
            for i in range(len(s)):
                if s[i]!=" ":
                    if s[i] not in lst:
                        lst.append(s[i])
                        lengths.append(len(lst))  
                    elif s[i] in lst and i+1==len(s):
                        lengths.append(len(lst))
                        lst=[]
                        lst.append(s[i])
                    elif s[i] in lst and i+1!=len(s):
                        lengths.append(len(lst))
                        index= lst.index(s[i])
                        lst=lst[index+1:]
                        lst.append(s[i])
                        lengths.append(len(lst))
                elif s.isspace():
                    lengths=[1]
                elif s[i]==" ":
                    lengths.append(len(lst))
                    lst=[]
                    lst.append(s[i])
            value=sorted(lengths)[-1]
        return value
