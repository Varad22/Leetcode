class Solution:
    def isValid(self, s: str) -> bool:
        symbols=[]
        for i in s:
            if i == "(" or i=="{" or i=="[":
                symbols.append(i)
            elif i==")" and symbols and symbols[-1]=="(":
                symbols.pop()
            elif i=="}" and symbols and symbols[-1]=="{":
                symbols.pop()
            elif i=="]" and symbols and symbols[-1]=="[":
                symbols.pop()
            else:
                return False
        if len(symbols)==0:
            return True
